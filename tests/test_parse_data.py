from gendiff.parse_data import generate_diff


f = open('./tests/fixtures/result.txt', 'r')
result = f.read()
f.close()


def test_json_files():
    assert result == generate_diff(
        './tests/fixtures/file1.json', './tests/fixtures/file2.json')


def test_yaml_files():
    assert result == generate_diff(
        './tests/fixtures/file1.yml', './tests/fixtures/file2.yml')
