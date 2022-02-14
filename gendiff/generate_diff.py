"""Generator of difference between two json files"""

import json


def generate_diff(file1, file2):
    s1 = json.load(open(file1))
    s2 = json.load(open(file2))
    com = s1.keys() & s2.keys()
    before = s1.keys() - s2.keys()
    after = s2.keys() - s1.keys()
    common = sorted(com)
    only_1 = sorted(before)
    only_2 = sorted(after)
    result = ['{', ]
    for i in common:
        if s1[i] == s2[i]:
            result.append('   ' + i + ': ' + str.lower(str(s1[i])))
        else:
            result.append(' - ' + i + ': ' + str.lower(str(s1[i])))
            result.append(' + ' + i + ': ' + str.lower(str(s2[i])))
    for i in only_1:
        result.append(' - ' + i + ': ' + str.lower(str(s1[i])))
    for i in only_2:
        result.append(' + ' + i + ': ' + str.lower(str(s2[i])))
    result.append('}')
    answer = ''
    for i in result:
        answer = answer + i + '\n'
    return answer
