import pytest
from gendiff.parse_data import parse_data
from gendiff.parse_data import format_output


f = open('./tests/fixtures/result.txt', 'r')
result = f.read()


def test_json_files():
    assert result == format_output(parse_data(
        './tests/fixtures/file1.json', './tests/fixtures/file2.json'))


def test_yaml_files():
    assert result == format_output(parse_data(
        './tests/fixtures/file1.yml', './tests/fixtures/file2.yml'))
