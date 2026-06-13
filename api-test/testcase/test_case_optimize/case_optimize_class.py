import allure
import pytest

from api.api import mobile_query
from utils.read import base_data

url = base_data.read_ini()['host']['api_sit_url']


@allure.epic("数据进制项目epic")
@allure.feature("手机号模块feature")
class TestMobile:
    @allure.story("杭州的手机号story")
    @allure.title("测试手机号归属地title")
    @allure.testcase("http://www.baidu.com", name="接口地址testcase")
    @allure.issue("http://www.baidu.com", name="缺陷地址issue")
    @allure.link("http://www.baidu.com", name="链接地址link")
    @allure.description("当前手机号是13456755448，归属地是杭州的description")
    @allure.step("先进性归属地的操作step")
    @allure.severity("critical")
    def test_mobile(self):
        param = base_data.read_data()["mobile_belong"]
        result = mobile_query(param)
        assert result.body['status'] == 0
        assert result.body['msg'] == "ok"
        assert result.body['result']["shouji"] == "13456755448"
        assert result.body['result']["province"] == "浙江"
        assert result.body['result']["city"] == "杭州"
        assert result.body['result']["company"] == "中国移动"
        assert result.body['result']["cardtype"] is None
        assert result.body['result']["areacode"] == "0571"

    @allure.story("杭州的手机号story")
    @allure.title("测试手机号归属地title")
    @allure.testcase("http://www.baidu.com", name="接口地址testcase")
    @allure.issue("http://www.baidu.com", name="缺陷地址issue")
    @allure.link("http://www.baidu.com", name="链接地址link")
    @allure.description("当前手机号是13456755448，归属地是杭州的description")
    @allure.step("先进性归属地的操作step")
    @allure.severity("critical")
    def test_mobile_dynamic(self):
        param = base_data.read_data()["mobile_belong_dynamic"]['params']
        title = base_data.read_data()["mobile_belong_dynamic"]['title']
        story = base_data.read_data()["mobile_belong_dynamic"]['story']
        allure.dynamic.title(title)
        allure.dynamic.story(story)
        result = mobile_query(param)
        assert result.body['status'] == 0
        assert result.body['msg'] == "ok"
        assert result.body['result']["shouji"] == "13456755448"
        assert result.body['result']["province"] == "浙江"
        assert result.body['result']["city"] == "杭州"
        assert result.body['result']["company"] == "中国移动"
        assert result.body['result']["cardtype"] is None
        assert result.body['result']["areacode"] == "0571"

    @allure.title("测试手机号mobile2")
    @allure.testcase("http://www.baidu.com", name="接口地址testcase")
    @allure.issue("http://www.baidu.com", name="缺陷地址issue")
    @allure.link("http://www.baidu.com", name="链接地址link")
    @allure.description("当前手机号是134000000000，归属地是安徽的description")
    @allure.step("先进行归属地的操作step")
    @allure.severity("blocker")
    def test_mobile2(self):
        param = base_data.read_data()["mobile_belong"]
        result = mobile_query(param)
        assert result['status'] == 0
        assert result['msg'] == "ok"
        assert result['result']["shouji"] == "13456755448"
        assert result['result']["province"] == "浙江12"
        assert result['result']["city"] == "杭州"
        assert result['result']["company"] == "中国移动"
        assert result['result']["cardtype"] is None
        assert result['result']["areacode"] == "0571"


if __name__ == '__main__':
    pytest.main()
