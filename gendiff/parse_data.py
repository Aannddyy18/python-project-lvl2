import yaml
import json


def parse_file(file, format):
    if format == 'yaml':
        f = yaml.safe_load(open(file))
        return f
    if format == 'json':
        f = json.load(open(file))
        return f
