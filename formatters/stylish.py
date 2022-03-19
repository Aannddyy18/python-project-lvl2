"""Convert dictionary to string"""
import json


def stylish(values, replacer=' ', spaces_count=2, lvl=1):
    if isinstance(values, dict):
        result = '{\n'
        for key, value in values.items():
            if isinstance(value, tuple):
                if value[0] == 'changed':
                    key_string = '- ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stringify_dict(value[1][0], replacer, spaces_count, lvl + 2) + '\n'
                    key_string = '+ ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stringify_dict(value[1][1], replacer, spaces_count, lvl + 2) + '\n'
                elif value[0] == 'deleted':
                    key_string = '- ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stringify_dict(value[1], replacer, spaces_count, lvl + 2) + '\n'
                elif value[0] == 'added':
                    key_string = '+ ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stringify_dict(value[1], replacer, spaces_count, lvl + 2) + '\n'
                elif value[0] == 'same':
                    key_string = '  ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stringify_dict(value[1], replacer, spaces_count, lvl + 2) + '\n'
                elif value[0] == 'nested':
                    key_string = '  ' + key
                    result += f'{replacer * spaces_count * lvl}{key_string}: '
                    result += stylish(value[1], replacer, spaces_count, lvl + 2) + '\n'
            else:
                return stringify_dict(value, replacer, spaces_count, lvl + 2)
        result += replacer * spaces_count * (lvl - 1) + '}'
    else:
        result = values if isinstance(values, str) else json.dumps(values)
    return result


def stringify_dict(values, replacer=' ', spaces_count=2, lvl=1):
    if isinstance(values, dict):
        result = '{\n'
        for key, value in values.items():
            key_string = '  ' + key
            result += f'{replacer * spaces_count * lvl}{key_string}: '
            result += stringify_dict(value, replacer, spaces_count, lvl + 2) + '\n'
        result += replacer * spaces_count * (lvl - 1) + '}'
    else:
        result = values if isinstance(values, str) else json.dumps(values)
    return result