import requests
import pytest

from api import api
from utils.read import base_data
from utils.read_data import get_data

url = base_data.read_ini()['host']['api_sit_url']


def test_mobile():
    param = base_data.read_data()["mobile_belong"]
    result = api.mobile_query(param['shouji'], param['appkey'])
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "浙江"
    assert result['result']["city"] == "杭州"
    assert result['result']["company"] == "中国移动"
    assert result['result']["cardtype"] is None
    assert result['result']["areacode"] == "0571"


@pytest.mark.parametrize("mobile,appkey", get_data["mobile_belong_get"])
def test_mobile_get(mobile, appkey):
    print("测试手机归属地get请求")
    result = api.mobile_query(mobile, appkey)
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "浙江"
    assert result['result']["city"] == "杭州"
    assert result['result']["company"] == "中国移动"
    assert result['result']["cardtype"] is None
    assert result['result']["areacode"] == "0571"



if __name__ == '__main__':
    pytest.main()
