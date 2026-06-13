import pytest


@pytest.fixture(scope="session")
def test_session():
    print("我是session级的fixture")


@pytest.fixture()
def get_mobile():
    params = {"shouji": "13456755448", "appkey": "0c818521d38759e1"}
    return params


# @pytest.fixture(scope="function")
# def func():
#     print("我是前置步骤，我需要先运行")
#     yield
#     print("我是后置步骤，我最后运行")

@pytest.fixture(scope="function")
def func():
    print("我是前置步骤，我需要先运行")
    yield "老武"
    print("我是后置步骤，我最后运行")
