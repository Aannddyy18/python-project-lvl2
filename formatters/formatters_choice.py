from formatters.stylish import stylish
from formatters.plain import simplify
from formatters.json_f import jsonf


def choose_format(dict, format_name):
    if format_name == 'stylish':
        return stylish(dict)
    elif format_name == 'plain':
        return simplify(dict)
    elif format_name == 'json':
        return jsonf(dict)
