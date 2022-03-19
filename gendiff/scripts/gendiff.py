#!/usr/bin/env python3
"""Parser and generator of difference between pair of json or yaml files"""
import argparse
from gendiff.gen_difference import generate_diff


def parse_command_line_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f', '--format', default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='set format of output'
    )
    parser.add_argument('first', metavar='first_file', type=str)
    parser.add_argument('second', metavar='second_file', type=str)

    args = parser.parse_args()
    return args


def main():
    args = parse_command_line_args()
    diff = generate_diff(args.first, args.second, args.format)
    print(diff)


if __name__ == '__main__':
    main()
