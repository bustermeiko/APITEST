import random
import time
import pytest
import yaml
from faker import Faker

from testcases.conftest import get_data
from utils.validate import extract_by_jsonpath

fake = Faker(locale="zh-CN")


def func_yaml(data, res=None):
    # isinstance判断数据类型，TRUE
    if isinstance(data, dict):
        for key, value in data.items():
            if '${' in str(value) and '}' in str(value):
                start = str(value).index('${')
                end = str(value).index('}')
                func_name = str(value)[start + 2:end]
                data[key] = str(value)[0:start] + str(eval(func_name)) + str(value)[end + 1:len(str(value))]
                # eval()函数的功能：将字符串str当成有效的表达式来求值并返回计算结果。
    return data


def random_name():
    # 随机电话号码，身份证等，需安装pip install Faker
    return fake.name()


def age():
    return random.randint(1, 100)


def random_number():
    # 随机电话号码，身份证等，需安装pip install Faker
    return random.randint(11, 1000000)


def local_time():
    return time.strftime('%Y%m%d-%H%M%S', time.localtime())


if __name__ == '__main__':
    # yaml中的定义的数据
    data = {
        "addroute": {
            "ID": "$.data.id",
            "Code": "TEST-${random_number()}",
            "Name": "test",
            "Version": 1,
            "IsVersion": False,
            "Status": 1
        }
    }

    # 接口返回的数据
    response = {'code': 200, 'data': {'id': 1329998882, 'message': 'ok'}}
    print(func_yaml(data['addroute'], response))
