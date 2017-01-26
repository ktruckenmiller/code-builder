import yaml
import json
import os

def open_file():
    with open("buildspec.yml", 'r') as f:
        read_data = f.read()
        return read_data
def test_yaml():
    print yaml.load(open_file())
