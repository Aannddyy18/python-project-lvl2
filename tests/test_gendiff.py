import pytest
import json
from gendiff.generate_diff import generate_diff


f = open('./tests/fixtures/expected.txt', 'r')
result = f.read()


def test_flat_files():
    assert result == generate_diff(
        './tests/fixtures/file1.json', './tests/fixtures/file2.json')
