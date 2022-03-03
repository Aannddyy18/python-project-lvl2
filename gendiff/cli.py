"""Command line interface"""
import argparse


def cli():
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


args = cli()
