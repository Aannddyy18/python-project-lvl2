"""Parser and generator iof difference between pair of json or yaml files"""
import yaml
import json
from collections import OrderedDict
from operator import itemgetter
from formatters.stylish import stylish
from formatters.plain import simplify
from formatters.json_f import jsonf


def generate_diff(file1, file2, format_name='stylish'):
    f1, f2 = how_to_open(file1, file2)

    def gen_diff_dict(f1, f2):
        common = f1.keys() & f2.keys()
        before = f1.keys() - f2.keys()
        after = f2.keys() - f1.keys()
        result = {}
        for i in common:
            if isinstance(f1[i], dict) and isinstance(f2[i], dict):
                result[('  ', i)] = gen_diff_dict(f1[i], f2[i])
            else:
                if f1[i] == f2[i]:
                    result[('  ', i)] = f1[i]
                else:
                    result[('- ', i)] = f1[i]
                    result[('+ ', i)] = f2[i]
        for i in before:
            result[('- ', i)] = f1[i]
        for i in after:
            result[('+ ', i)] = f2[i]
        result_keys = sorted(result.keys(), key=itemgetter(1))
        output_dict = OrderedDict.fromkeys(result_keys)
        for key in result_keys:
            output_dict[key] = result[key]
        return output_dict
    if format_name == 'stylish':
        return stylish(gen_diff_dict(f1, f2))
    if format_name == 'plain':
        return simplify(gen_diff_dict(f1, f2))
    if format_name == 'json':
        return jsonf(gen_diff_dict(f1, f2))


def how_to_open(file1, file2):
    if file1.endswith('.yml') or file1.endswith('.yaml'):
        f1 = yaml.safe_load(open(file1))
    else:
        f1 = json.load(open(file1))
    if file2.endswith('.yml') or file2.endswith('.yaml'):
        f2 = yaml.safe_load(open(file2))
    else:
        f2 = json.load(open(file2))
    return f1, f2
