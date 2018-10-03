# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from codecs import open
from builtins import str
from collections import OrderedDict
import yaml
import yamlordereddictloader

from open_api_schemas_to_markdown.translations import Translator


class Converter(object):
    def __init__(self, input_filepath, output_filepath, locale='en'):
        super(Converter, self).__init__()
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath
        self.locale = locale

    def convert(self):
        with open(self.input_filepath, 'r', encoding='utf-8') as f:
            content = yaml.load(f, Loader=yamlordereddictloader.Loader)

        self.ensure_openapi_3(content)

        res = []
        schemas = OrderedDict(content['components']['schemas'])
        for object_name, values in schemas.items():
            res.append(
                ObjectFormatter(object_name, values, self.locale).format()
            )

        with open(self.output_filepath, 'w', encoding='utf-8') as out:
            out.write(''.join(res))

    def ensure_openapi_3(self, content):
        if not content.get('openapi', '').startswith('3.'):
            raise ValueError('Expected an OpenAPI 3 specification file')


class ObjectFormatter(object):
    def __init__(self, object_name, values, locale):
        super(ObjectFormatter, self).__init__()
        self.object_name = object_name
        self.values = values
        self.locale = locale

    def format(self):
        res = [
            '## {name}'.format(name=self.object_name),
            self.table_header(),
            '|---|---|---|---|---|'
        ]
        for field, values in self.properties().items():
            template = '|{field}|{type}|{description}|{example}|{properties}|'.format(
                field=field,
                type=self.type(values),
                description=values.get('description', ''),
                example=str(values.get('example', '')),
                properties=self.field_properties(values)
            )
            res.append(template)
        return '\n'.join(res) + '\n'

    def table_header(self):
        translation = Translator.for_locale(self.locale)
        return '|{list}|'.format(
            list='|'.join([
                translation['field'],
                translation['type'],
                translation['description'],
                translation['example'],
                translation['properties'],
            ])
        )

    def properties(self):
        return self.values['properties']

    def field_properties(self, values):
        def beautify(value):
            if type(value) == list:
                return ', '.join(value)
            return value
        acc = OrderedDict()
        for k, v in OrderedDict(values).items():
            if k not in ['example', 'type', 'format', 'description']:
                acc[k] = v
        result = ['{}: {}'.format(k, beautify(v)) for k, v in acc.items()]
        return '<br>'.join(result)

    def type(self, values):
        if 'format' in values:
            return '{type}(${format})'.format(
                type=values['type'],
                format=values['format']
            )
        return values['type']
