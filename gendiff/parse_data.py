import yaml
import json


def parse_data(data, _format):
    if _format == 'yaml':
        f = yaml.safe_load(open(data))
        return f
    if _format == 'json':
        f = json.load(open(data))
        return f
