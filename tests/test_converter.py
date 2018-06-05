# -*- coding: utf-8 -*-
import unittest
import os.path as op
import os

from open_api_schemas_to_markdown.converter import Converter


def filepath(f):
    return op.join(op.abspath(op.join(__file__, op.pardir, op.pardir)), f)


class TestMain(unittest.TestCase):
    def test_check_for_open_api(self):
        in_file = filepath('tests/files/openapi_2_petstore_minimal.yml')

        with self.assertRaisesRegexp(ValueError, ''):
            Converter(in_file, '/tmp/out.md').convert()

    def test_simple_config(self):
        in_file = filepath('tests/files/simple_config.yml')
        expected_file = filepath('tests/files/expected_simple_config.md')

        self.run_for_files(in_file, expected_file)

    def test_simple_config_fr_locale(self):
        in_file = filepath('tests/files/simple_config.yml')
        expected_file = filepath('tests/files/expected_simple_config_fr.md')

        self.run_for_files(in_file, expected_file, locale='fr')

    def test_full_example(self):
        in_file = filepath('tests/files/full_example.yml')
        expected_file = filepath('tests/files/expected_full_example.md')

        self.run_for_files(in_file, expected_file)

    def run_for_files(self, in_file, expected_file, locale=None):
        out_file = '/tmp/out.md'

        if locale is None:
            Converter(in_file, out_file).convert()
        else:
            Converter(in_file, out_file, locale=locale).convert()

        self.assertEquals(
            open(out_file, 'r').readlines(),
            open(expected_file, 'r').readlines(),
        )

        os.remove(out_file)
