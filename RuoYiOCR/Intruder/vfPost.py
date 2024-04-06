from RuoYiOCR.Intruder.getCapImg import decode_base64_to_img
from RuoYiOCR.Intruder.getRuoYiCap import get_captcha


def vfPost():
    getCaptcha1 = get_captcha('http://127.0.0.1/dev-api/captchaImage').json()
    decode_base64_to_img(getCaptcha1['img'])
    vfPost()
    return getCaptcha1
