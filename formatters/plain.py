"""Convert dictionary of difference to simple description"""
import json


def stringify(diff_dict):
    return (walk_on_dict(diff_dict, '')).strip('\n')


def stringify_value(item):
    if isinstance(item, dict):
        return '[complex value]'
    else:
        return f'\'{item}\'' if isinstance(item, str) else json.dumps(item)


def walk_on_dict(node, path):
    result = ''
    for key, value in node.items():
        prop_name = (path + '.' + key).strip('.')
        if value[0] == 'changed':
            result += f'Property \'{prop_name}\' was updated. From {stringify_value(value[1][0])} ' \
                      f'to {stringify_value(value[1][1])}\n'
        elif value[0] == 'deleted':
            result += f'Property \'{prop_name}\' was removed\n'
        elif value[0] == 'added':
            result += f'Property \'{prop_name}\' was added with value: {stringify_value(value[1])}\n'
        elif value[0] == 'nested':
            result += walk_on_dict(value[1], path + '.' + key)
    return result
