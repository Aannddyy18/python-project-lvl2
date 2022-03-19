"""Generator of difference between pair of dictionaries"""


def gen_diff_dict(f1, f2):
    common = f1.keys() & f2.keys()
    before = f1.keys() - f2.keys()
    after = f2.keys() - f1.keys()
    result = {}
    for i in common:
        if isinstance(f1[i], dict) and isinstance(f2[i], dict):
            result[i] = ('nested', gen_diff_dict(f1[i], f2[i]))
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
