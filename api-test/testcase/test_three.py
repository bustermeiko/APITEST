import pytest


@pytest.mark.pro
class TestThree:
    # def setup_method(self):
    #     print("测试之前要进行的事情")
    #
    # def teardown_method(self):
    #     print("测试之后要进行的事情")

    # def setup_class(self):
    #     print("测试之前要进行的事情")
    #
    # def teardown_class(self):
    #     print("测试之后要进行的事情")

    def test_one(self):
        print("测试1==1")
        expect = 1
        actual = 1
        assert expect == actual

    def test_two(self):
        print("测试2==2")
        expect = 2
        actual = 2
        assert expect == actual
