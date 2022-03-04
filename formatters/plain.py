"""Convert dictionary of difference to simple description"""
import json


def simplify(values):
    def walk_on_dict(node, path):
        result = ''
        if isinstance(node, dict):
            key_tuples = node.keys()
            for key in key_tuples:
                if key[0] == '- ' and ('+ ', key[1]) in key_tuples:
                    new_key = ('+ ', key[1])
                    prop_name = (path + '.' + key[1]).strip('.')
                    result += f'Property \'{prop_name}\' was updated. From {check_item(node[key])} ' \
                              f'to {check_item(node[new_key])}\n'
                elif key[0] == '- ' and ('+ ', key[1]) not in key_tuples:
                    prop_name = (path + '.' + key[1]).strip('.')
                    result += f'Property \'{prop_name}\' was removed\n'
                elif key[0] == '+ ' and ('- ', key[1]) not in key_tuples:
                    prop_name = (path + '.' + key[1]).strip('.')
                    result += f'Property \'{prop_name}\' was added with value: {check_item(node[key])}\n'
                if isinstance(node[key], dict):
                    result += walk_on_dict(node[key], path + '.' + key[1])
        return result

    return (walk_on_dict(values, '')).strip('\n')


def check_item(item):
    if isinstance(item, dict):
        return '[complex value]'
    else:
        return f'\'{item}\'' if isinstance(item, str) else json.dumps(item)
