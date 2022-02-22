"""Convert dictionary to string""" 

def stylish(values, replacer=' ', spaces_count=2, lvl=1, flag=''):
    if isinstance(values, dict):
        result = '{\n'
        key_string = ''
        for key, value in values.items():
            if key[0] == '+ ' or key[0] == '- ' or key[0] == '  ':
                key_string = ''.join(key)
            else:
                key_string = '  ' + ''.join(key)
            result += f'{replacer * spaces_count * lvl}{key_string}: '
            if key_string.startswith(('+', '-')):
                result += stylish(value, replacer, spaces_count, lvl + 2, flag='new') + '\n'
            else:
                result += stylish(value, replacer, spaces_count, lvl + 2) + '\n'
        if flag == 'new':
            result += replacer * spaces_count * (lvl - 1) + '}'
        else:
            result += replacer * spaces_count * (lvl - 1) + '}'
    else:
        result = str(values)
    return result
