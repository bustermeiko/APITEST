from core.api_util import api_util
from utils.response_util import process_response


def send_code(json_data):
    """
    获取短信验证码
    :param json_data:
    :return:
    """
    response = api_util.get_code(json=json_data)
    return process_response(response)


def register(code, mobile):
    """
    注册接口
    :param code:
    :param mobile:
    :return:
    """
    json_data = {
        "code": str(code),
        "password": "123456",
        "username": str(mobile)
    }
    response = api_util.register_mobile(json=json_data)
    return process_response(response)


def login(username, password):
    """
    用户登录接口
    :param username:
    :param password:
    :return:
    """
    json_data = {
        "username": username, "password": password
    }
    response = api_util.user_login(json=json_data)
    return process_response(response)


def add_shopping_cart(params, token):
    """
    添加购物车
    :param token:
    :param params:
    :return:
    """
    headers = {
        "Authorization": "JWT " + token
    }
    response = api_util.shopping_add(json=params, headers=headers)
    return process_response(response)


def add_message(data, files, token):
    """
    增加留言
    :param data:
    :param files:
    :param token:
    :return:
    """
    headers = {
        "Authorization": "JWT " + token
    }
    response = api_util.add_message(data=data,files=files,headers=headers)
    return process_response(response)


def add_shopping_cart2(params, headers):
    """
    添加购物车
    :param headers:
    :param params:
    :return:
    """
    response = api_util.shopping_add(json=params, headers=headers)
    return process_response(response)


def add_message2(data, files, headers):
    """
    增加留言
    :param headers:
    :param data:
    :param files:
    :return:
    """
    response = api_util.add_message(data=data,files=files,headers=headers)
    return process_response(response)
