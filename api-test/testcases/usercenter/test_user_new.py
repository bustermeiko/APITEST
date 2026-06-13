import allure
import pytest

from core.ApiService import ApiService
from utils.YamlUtil import YamlUtil


@allure.feature("用户中心模块")
class TestUser:
    @pytest.mark.parametrize("data", YamlUtil().extract_case("user_center.yaml", 'user_login_new'))
    def test_user_new(self, data):
        ApiService().handle_case(data)