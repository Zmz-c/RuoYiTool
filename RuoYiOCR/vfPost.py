from RuoYiOCR.getCapImg import decode_base64_to_img
from RuoYiOCR.getRuoYiCap import get_captcha
from RuoYiOCR.main.Vf import verification
from RuoYiOCR.main.json_data import json_data


def vfPost():
    getCaptcha1 = get_captcha('http://127.0.0.1/dev-api/captchaImage').json()
    decode_base64_to_img(getCaptcha1['img'])
    vfPost()
    return getCaptcha1
