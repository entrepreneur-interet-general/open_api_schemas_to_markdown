# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Translator(object):
    MAPPING = {
        'en': {
            'field': 'Field',
            'type': 'Type',
            'description': 'Description',
            'example': 'Example',
            'properties': 'Properties',
        },
        'fr': {
            'field': 'Colonne',
            'type': 'Type',
            'description': 'Description',
            'example': 'Exemple',
            'properties': 'Propriétés',
        }
    }

    def __init__(self):
        super(Translator, self).__init__()

    @staticmethod
    def for_locale(locale):
        if locale not in Translator.available_locales():
            message = 'Locale not found. Supported locales: {locales}'.format(
                locales=Translator.available_locales_str()
            )
            raise NotImplementedError(message)
        return Translator.MAPPING[locale]

    @staticmethod
    def available_locales():
        return sorted(Translator.MAPPING.keys())

    @staticmethod
    def available_locales_str():
        return ', '.join(Translator.available_locales())
