from RuoYiOCR.getCapImg import decode_base64_to_img
from RuoYiOCR.getRuoYiCap import get_captcha
from RuoYiOCR.main.Vf import verification
from RuoYiOCR.main.json_data import json_data


def PostDate(username, password):
    getCaptcha = get_captcha('http://127.0.0.1/dev-api/captchaImage').json()
    decode_base64_to_img(getCaptcha['img'])
    verification()
    date3 = {
        'username': username,
        'password': password
    }
    data = merge(verification(), date3)
    json_data(data)


def merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
