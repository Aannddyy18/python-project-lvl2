"""Convert dictionary to string"""
import json


def stylish(values, replacer=' ', spaces_count=2, lvl=1):
    if isinstance(values, dict):
        result = '{\n'
        for key, value in values.items():
            if key[0] == '+ ' or key[0] == '- ' or key[0] == '  ':
                key_string = ''.join(key)
            else:
                key_string = '  ' + ''.join(key)
            result += f'{replacer * spaces_count * lvl}{key_string}: '
            result += stylish(value, replacer, spaces_count, lvl + 2) + '\n'
        result += replacer * spaces_count * (lvl - 1) + '}'
    else:
        result = values if isinstance(values, str) else json.dumps(values)
    return result