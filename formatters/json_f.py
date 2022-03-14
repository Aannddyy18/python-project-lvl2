"""Convert dictionary of difference to json format"""
import json


def jsonf(values, replacer=' ', spaces_count=2, lvl=1):

    def make_json(values, replacer=' ', spaces_count=2, lvl=1):
        if isinstance(values, dict):
            last = next(reversed(values))
            result = '{\n'
            for key, value in values.items():
                key_string = (''.join(key)).strip(' ')
                result += f'{replacer * spaces_count * lvl}\"{key_string}\": '
                if len(values) > 1:
                    if key == last:
                        result += make_json(value, replacer, spaces_count, lvl + 1) + '\n'
                    else:
                        result += make_json(value, replacer, spaces_count, lvl + 1) + ',' + '\n'
                else:
                    result += make_json(value, replacer, spaces_count, lvl + 1) + '\n'
            result += replacer * spaces_count * (lvl - 1) + '}'
        else:
            result = f'\"{values}\"' if isinstance(values, str) else json.dumps(values)
        return result

    if isinstance(values, dict):
        last = next(reversed(values))
        result = '{\n'
        for key, value in values.items():
            if isinstance(value, tuple):
                if value[0] == 'added':
                    key_string = ('+' + ''.join(key)).strip(' ')
                    result += f'{replacer * spaces_count * lvl}\"{key_string}\": '
                    if len(values) > 1:
                        if key == last:
                            result += make_json(value[1], replacer, spaces_count, lvl + 1) + '\n'
                        else:
                            result += make_json(value[1], replacer, spaces_count, lvl + 1) + ',' + '\n'
                    else:
                        result += make_json(value[1], replacer, spaces_count, lvl + 1) + '\n'
                elif value[0] == 'changed':
                    key_string = ('-' + ''.join(key)).strip(' ')
                    result += f'{replacer * spaces_count * lvl}\"{key_string}\": '
                    result += make_json(value[1][0], replacer, spaces_count, lvl + 1) + ',' + '\n'
                    key_string = ('+' + ''.join(key)).strip(' ')
                    result += f'{replacer * spaces_count * lvl}\"{key_string}\": '
                    if len(values) > 1:
                        if key == last:
                            result += make_json(value[1][1], replacer, spaces_count, lvl + 1) + '\n'
                        else:
                            result += make_json(value[1][1], replacer, spaces_count, lvl + 1) + ',' + '\n'
                    else:
                        result += make_json(value[1][1], replacer, spaces_count, lvl + 1) + '\n'
                elif value[0] == 'deleted':
                    key_string = ('-' + ''.join(key)).strip(' ')
                    result += f'{replacer * spaces_count * lvl}\"{key_string}\": '
                    if len(values) > 1:
                        if key == last:
                            result += make_json(value[1], replacer, spaces_count, lvl + 1) + '\n'
                        else:
                            result += make_json(value[1], replacer, spaces_count, lvl + 1) + ',' + '\n'
                    else:
                        result += make_json(value[1], replacer, spaces_count, lvl + 1) + '\n'
                elif value[0] == 'same':
                    key_string = (''.join(key)).strip(' ')
                    result += f'{replacer * spaces_count * lvl}\"{key_string}\": '
                    if len(values) > 1:
                        if key == last:
                            result += jsonf(value[1], replacer, spaces_count, lvl + 1) + '\n'
                        else:
                            result += jsonf(value[1], replacer, spaces_count, lvl + 1) + ',' + '\n'
                    else:
                        result += jsonf(value[1], replacer, spaces_count, lvl + 1) + '\n'
            else:
                return make_json(value, replacer, spaces_count, lvl + 1)
        result += replacer * spaces_count * (lvl - 1) + '}'
    else:
        result = f'\"{values}\"' if isinstance(values, str) else json.dumps(values)
    return result
