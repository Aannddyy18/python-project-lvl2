"""Parser and generator iof difference between pair of json or yaml files"""
import yaml
import json
from formatters.stylish import stylish
from formatters.plain import simplify
from formatters.json_f import jsonf


def generate_diff(file1, file2, format_name='stylish'):
    f_1, format_1 = read_file(file1)
    f_2, format_2 = read_file(file2)
    f1 = parse_file(f_1, format_1)
    f2 = parse_file(f_2, format_2)

    def gen_diff_dict(f1, f2):
        common = f1.keys() & f2.keys()
        before = f1.keys() - f2.keys()
        after = f2.keys() - f1.keys()
        result = {}
        for i in common:
            if isinstance(f1[i], dict) and isinstance(f2[i], dict):
                result[i] = ('same', gen_diff_dict(f1[i], f2[i]))
            elif f1[i] == f2[i]:
                result[i] = ('same', f1[i])
            else:
                result[i] = ('changed', (f1[i], f2[i]))
        for i in before:
            result[i] = ('deleted', f1[i])
        for i in after:
            result[i] = ('added', f2[i])
        result_keys = sorted(result.keys())
        output_dict = dict.fromkeys(result_keys)
        for key in result_keys:
            output_dict[key] = result[key]
        return output_dict
    if format_name == 'stylish':
        return stylish(gen_diff_dict(f1, f2))
    if format_name == 'plain':
        return simplify(gen_diff_dict(f1, f2))
    if format_name == 'json':
        return jsonf(gen_diff_dict(f1, f2))


def read_file(f):
    if f.endswith('.yml') or f.endswith('.yaml'):
        return f, 'yaml'
    if f.endswith('.json'):
        return f, 'json'


def parse_file(file, format):
    if format == 'yaml':
        f = yaml.safe_load(open(file))
        return f
    if format == 'json':
        f = json.load(open(file))
        return f
