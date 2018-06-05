# -*- coding: utf-8 -*-
import unittest

from open_api_schemas_to_markdown.translations import Translator


class TestMain(unittest.TestCase):
    def test_mapping(self):
        for locale, v in Translator.MAPPING.items():
            self.assertEquals(
                sorted(v.keys()),
                ['description', 'example', 'field', 'properties', 'type'],
                'Wrong keys for locale ' + locale
            )

    def test_for_locale(self):
        self.assertEquals(
            Translator.for_locale('en'),
            {
                'description': 'Description',
                'example': 'Example',
                'field': 'Field',
                'properties': 'Properties',
                'type': 'Type'
            }
        )

    def test_for_locale_not_found(self):
        with self.assertRaisesRegexp(NotImplementedError, r'^Locale not found. Supported locales:'):
            Translator.for_locale('it')
