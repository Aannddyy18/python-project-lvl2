import os
from os.path import dirname
import pytest
from gendiff.scripts.gendiff import generate_diff


FIXTURES_FOLDER = 'fixtures'

f = open(os.path.join(dirname(__file__), FIXTURES_FOLDER, 'expected_nested.txt'), 'r')
result = f.read()
f.close()

f_plain = open(os.path.join(dirname(__file__), FIXTURES_FOLDER, 'expected_plain.txt'), 'r')
result_plain = f_plain.read()
f_plain.close()

f_json = open(os.path.join(dirname(__file__), FIXTURES_FOLDER, 'expected_json.txt'), 'r')
result_json = f_json.read()
f_json.close()

f1_json_nested = os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file1_nested.json')
f2_json_nested = os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file2_nested.json')
f1_yaml_nested = os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file1_nested.yml')
f2_yaml_nested = os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file2_nested.yml')

testdata = [
    (f1_json_nested, f2_json_nested, 'stylish', result),
    (f1_yaml_nested, f2_yaml_nested, 'stylish', result),
    (f1_json_nested, f2_json_nested, 'plain', result_plain),
    (f1_yaml_nested, f2_yaml_nested, 'plain', result_plain),
    (f1_json_nested, f2_json_nested, 'json', result_json),
    (f1_yaml_nested, f2_yaml_nested, 'json', result_json)
]


@pytest.mark.parametrize("a, b, f, expected", testdata)
def test_gendiff(a, b, f, expected):
    assert generate_diff(a, b, f) == expected
