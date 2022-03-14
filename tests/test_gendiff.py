import os
from os.path import dirname
import pytest
from gendiff.scripts.gendiff import generate_diff


FIXTURES_FOLDER = 'fixtures'


def get_content(path_to_file):
    with open(path_to_file, "r") as f:
        return f.read()


result = get_content(os.path.join(dirname(__file__), FIXTURES_FOLDER, 'expected_nested.txt'))

result_plain = get_content(os.path.join(dirname(__file__), FIXTURES_FOLDER, 'expected_plain.txt'))

result_json = get_content(os.path.join(dirname(__file__), FIXTURES_FOLDER, 'expected_json.txt'))

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
