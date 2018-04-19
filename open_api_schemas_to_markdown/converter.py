# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from codecs import open
from collections import OrderedDict
import yaml


class Converter(object):
    def __init__(self, input_filepath, output_filepath):
        super(Converter, self).__init__()
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath

    def convert(self):
        with open(self.input_filepath, 'r', encoding='utf-8') as f:
            content = yaml.safe_load(f)

        res = []
        for object_name, values in content['components']['schemas'].iteritems():
            res.append(ObjectFormatter(object_name, values).format())

        with open(self.output_filepath, 'w', encoding='utf-8') as out:
            out.write(''.join(res))


class ObjectFormatter(object):
    def __init__(self, object_name, values):
        super(ObjectFormatter, self).__init__()
        self.object_name = object_name
        self.values = values

    def format(self):
        res = [
            '## {name} Model'.format(name=self.object_name),
            '|Field|Type|Description|Example|Properties|',
            '|---|---|---|---|---|'
        ]
        for field, values in self.properties().iteritems():
            template = '|{field}|{type}|{description}|{example}|{properties}|'.format(
                field=field,
                type=self.type(values),
                description=values.get('description', ''),
                example=unicode(values.get('example', '')),
                properties=self.field_properties(values)
            )
            res.append(template)
        return '\n'.join(res) + '\n'

    def properties(self):
        return self.values['properties']

    def field_properties(self, values):
        res = OrderedDict()
        for k, v in values.iteritems():
            if k not in ['example', 'type', 'format', 'description']:
                res[k] = v
        return '<br>'.join(['{}: {}'.format(k, v) for k, v in res.iteritems()])

    def type(self, values):
        if 'format' in values:
            return '{type}(${format})'.format(
                type=values['type'],
                format=values['format']
            )
        return values['type']
