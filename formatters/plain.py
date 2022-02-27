"""Convert dictionary of difference to simple description"""
import json


def simplify(values):
    def walk_on_dict(node, path):
        result = ''
        keys = set()
        for k, v in node.items():
            sign = k[0]
            keyname = k[1]
            if isinstance(v, dict):
                walk_on_dict(v, path + '.' + keyname)
            elif sign != '  ':
                keys.add(keyname)
        for k in keys:
            if ('- ', k) in node and ('+ ', k) in node:
                result += 'Property \'{}\' was updated. From {} to {}\n'.format(
                    (path + '.' + k).strip('.'), check_item(node[('- ', k)]), check_item(node[('+ ', k)])
                    )
            elif ('- ', k) in node:
                result += 'Property \'{}\' was removed\n'.format((path + '.' + k).strip('.'))
            elif ('+ ', k) in node:
                result += 'Property \'{}\' was added with value: {}\n'.format(
                        (path + '.' + k).strip('.'), check_item(node[('+ ', k)])
                    )
        return result.strip(' ')
    return walk_on_dict(values, '')


def check_item(item):
    if isinstance(item, dict):
        return '[complex value]'
    else:
        return f'\'{item}\'' if isinstance(item, str) else json.dumps(item)
