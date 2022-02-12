"""Generator of difference between two json files"""

import json


def generate_diff(file1, file2):
    source1 = json.load(open(file1))
    source2 = json.load(open(file2))
    result = '{' + '\n'
    for i in source1.keys() & source2.keys():
        if source1[i] == source2[i]:
            result = result + '   ' + i + ': ' + str(source1[i]) + '\n'
        else:
            result = result + ' - ' + i + ': ' + str(source1[i]) + '\n'
            result = result + ' + ' + i + ': ' + str(source2[i]) + '\n'
    for i in source1.keys() - source2.keys():
        result = result + ' - ' + i + ': ' + str(source1[i]) + '\n'
    for i in source2.keys() - source1.keys():
        result = result + ' + ' + i + ': ' + str(source2[i]) + '\n'
    result = result + '}'
    return result
