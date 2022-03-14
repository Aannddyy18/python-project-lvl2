"""Convert dictionary of difference to simple description"""
import json


def simplify(values):
    def walk_on_dict(node, path):
        result = ''
        if isinstance(node, dict):
            for key, value in node.items():
                if value[0] == 'changed':
                    prop_name = (path + '.' + key).strip('.')
                    result += f'Property \'{prop_name}\' was updated. From {check_item(value[1][0])} ' \
                              f'to {check_item(value[1][1])}\n'
                elif value[0] == 'deleted':
                    prop_name = (path + '.' + key).strip('.')
                    result += f'Property \'{prop_name}\' was removed\n'
                elif value[0] == 'added':
                    prop_name = (path + '.' + key).strip('.')
                    result += f'Property \'{prop_name}\' was added with value: {check_item(value[1])}\n'
                if value[0] == 'same' and isinstance(value[1], dict):
                    result += walk_on_dict(value[1], path + '.' + key)
        return result

    return (walk_on_dict(values, '')).strip('\n')


def check_item(item):
    if isinstance(item, dict):
        return '[complex value]'
    else:
        return f'\'{item}\'' if isinstance(item, str) else json.dumps(item)
