import pytest


# 数组的形式
# @pytest.mark.parametrize("name,word", [["安琪拉", "火烧屁屁咯"], ["黄忠", "周日被我射熄火了"], ["鲁班", "上上下下左左右右"]])
# def test_parametrize_02(name, word):
#     print(f'{name}的台词是{word}')

# 元组的形式
# @pytest.mark.parametrize("name,word", [("安琪拉", "火烧屁屁咯"), ("黄忠", "周日被我射熄火了"), ("鲁班", "上上下下左左右右")])
# def test_parametrize_02(name, word):
#     print(f'{name}的台词是{word}')

@pytest.mark.parametrize("name,word", [["安琪拉", "火烧屁屁咯"]])
def test_parametrize_02(name, word):
    print(f'{name}的台词是{word}')

