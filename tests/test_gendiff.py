import os
from os.path import dirname
import pytest
from gendiff.generate_diff import generate_diff
from gendiff.stylish import stylish


FIXTURES_FOLDER = 'fixtures'

f = open(os.path.join(dirname(__file__), FIXTURES_FOLDER, 'expected_nested.txt'), 'r')
result = f.read()



def test_json_files():
    assert result == stylish(generate_diff(
           os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file1_nested.json'),
        os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file2_nested.json')))

def test_yaml_files():
    assert result == stylish(generate_diff(
            os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file1_nested.yml'),
        os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file2_nested.yml')))
