import os
from os.path import dirname
import pytest
from gendiff.generate_diff import generate_diff


FIXTURES_FOLDER = 'fixtures'

f = open(os.path.join(dirname(__file__), FIXTURES_FOLDER, 'expected_nested.txt'), 'r')
result = f.read()

f_plain = open(os.path.join(dirname(__file__), FIXTURES_FOLDER, 'expected_plain.txt'), 'r')
result_plain = f_plain.read()

def test_json_files():
    assert result == generate_diff(
        os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file1_nested.json'),
        os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file2_nested.json'), 'stylish'
    )

def test_yaml_files():
    assert result == generate_diff(
        os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file1_nested.yml'),
        os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file2_nested.yml'), 'stylish'
    )

def test_plain_json():
    assert result_plain == generate_diff(
        os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file1_nested.json'),
        os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file2_nested.json'), 'plain'
    )

def test_plain_yaml():
    assert result_plain == generate_diff(
        os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file1_nested.yml'),
        os.path.join(dirname(__file__), FIXTURES_FOLDER, 'file2_nested.yml'), 'plain'
    )