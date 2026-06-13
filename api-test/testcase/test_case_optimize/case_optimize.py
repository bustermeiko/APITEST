import pytest

from api.api import mobile_query
from utils.read import base_data

url = base_data.read_ini()['host']['api_sit_url']


def test_mobile():
    param = base_data.read_data()["mobile_belong"]
    result = mobile_query(param)
    assert result.success is True
    assert result.body['status'] == 0
    assert result.body['msg'] == "ok"
    assert result.body['result']["shouji"] == "13456755448"
    assert result.body['result']["province"] == "浙江"
    assert result.body['result']["city"] == "杭州"
    assert result.body['result']["company"] == "中国移动"
    assert result.body['result']["cardtype"] is None
    assert result.body['result']["areacode"] == "0571"


if __name__ == '__main__':
    pytest.main()
