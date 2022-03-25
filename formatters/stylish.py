"""Convert dictionary to string"""
import json


def stylish(values, lvl=0):
    replacer = ' '
    spaces_count = 4
    if isinstance(values, dict):
        result = '{\n'
        for key, value in values.items():
            if isinstance(value, tuple):
                if value[0] == 'changed':
                    key_string = '  - ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stringify_dict(value[1][0], lvl + 1) + '\n'
                    key_string = '  + ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stringify_dict(value[1][1], lvl + 1) + '\n'
                elif value[0] == 'deleted':
                    key_string = '  - ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stringify_dict(value[1], lvl + 1) + '\n'
                elif value[0] == 'added':
                    key_string = '  + ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stringify_dict(value[1], lvl + 1) + '\n'
                elif value[0] == 'same':
                    key_string = '    ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stringify_dict(value[1], lvl + 1) + '\n'
                elif value[0] == 'nested':
                    key_string = '    ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stylish(value[1], lvl + 1) + '\n'
            else:
                return stringify_dict(value, lvl + 1)
        result += replacer * spaces_count * lvl + '}'
    else:
        result = values if isinstance(values, str) else json.dumps(values)
    return result


def stringify_dict(values, lvl=0):
    replacer = ' '
    spaces_count = 4
    if isinstance(values, dict):
        result = '{\n'
        for key, value in values.items():
            key_string = '    ' + key
            result += f'{replacer * spaces_count * lvl}{key_string}: '
            result += stringify_dict(value, lvl + 1) + '\n'
        result += replacer * spaces_count * lvl + '}'
    else:
        result = values if isinstance(values, str) else json.dumps(values)
    return result
