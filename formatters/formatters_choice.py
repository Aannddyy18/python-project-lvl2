from typing import Literal
from formatters.stylish import stylish
from formatters.plain import stringify
from formatters.json_f import jsonf


def choose_and_format(diff_dict, format_name: Literal['stylish', 'plain', 'json']) -> None:
    if format_name == 'stylish':
        return stylish(diff_dict)
    elif format_name == 'plain':
        return stringify(diff_dict)
    elif format_name == 'json':
        return jsonf(diff_dict)
