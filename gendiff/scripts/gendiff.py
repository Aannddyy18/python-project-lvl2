#!/usr/bin/env python3

import argparse
from gendiff.parse_data import parse_data
from gendiff.parse_data import format_output


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first', metavar='first_file', type=str)
    parser.add_argument('second', metavar='second_file', type=str)

    args = parser.parse_args()

    diff = format_output(parse_data(args.first, args.second))
    print(diff)


if __name__ == '__main__':
    main()
