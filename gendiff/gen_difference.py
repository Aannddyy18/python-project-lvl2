"""Parser and generator of difference between pair of json or yaml files"""
from formatters.formatters_choice import choose_and_format
from gendiff.read_data import read_data
from gendiff.parse_data import parse_data
from gendiff.gendiff_dict import gen_diff_dict


def generate_diff(file1, file2, format_name='stylish'):
    f_1, format_1 = read_data(file1)
    f_2, format_2 = read_data(file2)
    f1 = parse_data(f_1, format_1)
    f2 = parse_data(f_2, format_2)
    return choose_and_format(gen_diff_dict(f1, f2), format_name)
