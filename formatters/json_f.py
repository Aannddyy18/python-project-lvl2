"""Convert dictionary of difference to json format"""
import json


def jsonf(values, replacer=' ', spaces_count=2, lvl=1):
    if isinstance(values, dict):
        last = next(reversed(values))
        result = '{\n'
        for key, value in values.items():
            if key[0] == '+ ':
                key_string = ('+' + ''.join(key[1])).strip(' ')
            elif key[0] == '- ':
                key_string = ('-' + ''.join(key[1])).strip(' ')
            else:
                key_string = ('' + ''.join(key)).strip(' ')
            if len(values) > 1:
                result += f'{replacer * spaces_count * lvl}\"{key_string}\": '
                if key == last:
                    result += jsonf(value, replacer, spaces_count, lvl + 1) + '\n'
                else:
                    result += jsonf(value, replacer, spaces_count, lvl + 1) + ',' + '\n'
            else:
                result += f'{replacer * spaces_count * lvl}\"{key_string}\": '
                result += jsonf(value, replacer, spaces_count, lvl + 1) + '\n'
        result += replacer * spaces_count * (lvl - 1) + '}'
    else:
        result = f'\"{values}\"' if isinstance(values, str) else json.dumps(values)
    return result