import pytest
from gendiff.generate_diff import generate_diff
from gendiff.stylish import stylish


f = open('./tests/fixtures/expected_nested.txt', 'r')
result = f.read()



def test_json_files():
    assert result == stylish(generate_diff(
           './tests/fixtures/file1_nested.json', './tests/fixtures/file2_nested.json'))


def test_yaml_files():
    assert result == stylish(generate_diff(
           './tests/fixtures/file1_nested.yml', './tests/fixtures/file2_nested.yml'))
