import configparser
import os
import yaml

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")


def read_data():
    f = open(data_path, encoding="utf-8")
    data = yaml.safe_load(f)
    print(data)
    return data


get_data = read_data()
