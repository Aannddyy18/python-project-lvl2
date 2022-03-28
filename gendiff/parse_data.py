import yaml
import json


def parse_data(_data, _format):
    if _format == 'yaml':
        f = yaml.safe_load(_data)
        return f
    if _format == 'json':
        f = json.load(_data)
        return f
