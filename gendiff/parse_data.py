"""Parser and generator of difference between pair of json or yaml files"""
import yaml
import json
from collections import OrderedDict
from operator import itemgetter


def parse_data(file1, file2):
    if file1.endswith('.yml') or file1.endswith('.yaml'):
        f1 = yaml.safe_load(open(file1))
    else:
        f1 = json.load(open(file1))
    if file2.endswith('.yml') or file2.endswith('.yaml'):
        f2 = yaml.safe_load(open(file2))
    else:
        f2 = json.load(open(file2))
    common = f1.keys() & f2.keys()
    before = f1.keys() - f2.keys()
    after = f2.keys() - f1.keys()
    result = {}
    for i in common:
        if f1[i] == f2[i]:
            result[('    ', i)] = str.lower(str(f1[i]))
        else:
            result[('  - ', i)] = str.lower(str(f1[i]))
            result[('  + ', i)] = str.lower(str(f2[i]))
    for i in before:
        result[('  - ', i)] = str.lower(str(f1[i]))
    for i in after:
        result[('  + ', i)] = str.lower(str(f2[i]))
    result_keys = sorted(result.keys(), key=itemgetter(1))
    output_dict = OrderedDict.fromkeys(result_keys)
    for key in result_keys:
        output_dict[key] = result[key]
    return output_dict


def format_output(dictionary=OrderedDict):
    result_list = ['{', ]
    key_string = ''
    for key in dictionary:
        key_string = ''.join(key)
        result_list.append(key_string + ': ' + dictionary[key])
    result_list.append('}')
    result_text = ''
    for i in result_list:
        result_text = result_text + i + '\n'
    return result_text
