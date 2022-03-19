"""Convert dictionary of difference to json format"""
import json


def jsonf(values):
    return json.dumps(values, indent=2)
