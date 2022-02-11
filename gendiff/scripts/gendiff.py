#!/usr/bin/env python3

import argparse
import pathlib

def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('source_file', metavar='first_file', type=open)
    parser.add_argument('source_file', metavar='second_file', type=open)

    args = parser.parse_args()


if __name__ == '__main__':
    main()
