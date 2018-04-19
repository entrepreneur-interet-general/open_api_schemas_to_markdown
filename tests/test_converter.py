# -*- coding: utf-8 -*-
import unittest
import filecmp
import os.path as op

from open_api_schemas_to_markdown.converter import Converter


def filepath(f):
    return op.join(op.abspath(op.join(__file__, op.pardir, op.pardir)), f)


class TestMain(unittest.TestCase):
    def test_depreciation_value(self):
        in_file = filepath('tests/files/simple_config.yml')
        expected_file = filepath('tests/files/expected_simple_config.md')
        out_file = '/tmp/out.md'
        Converter(in_file, out_file).convert()

        self.assertEquals(
            open(out_file, 'r').readlines(),
            open(expected_file, 'r').readlines(),
        )
