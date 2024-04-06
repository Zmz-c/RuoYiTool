import ddddocr

from RuoYiOCR.getCapImg import decode_base64_to_img
from RuoYiOCR.getRuoYiCap import get_captcha
from RuoYiOCR.getUsername import getUsername

global result, getCaptcha
global uuid


def verification():
    # 验证码识别
    global result, getCaptcha
    global uuid
    ocr = ddddocr.DdddOcr()

    with open('image.jpg', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    text = res[:3]
    if "+" in text or "-" in text or "*" in text or "/" in text:
        first_char = text[0]
        last_char = text[-1]
        if "+" in text:
            try:
                result = int(first_char) + int(last_char)
            except ValueError:
                result = False
        if "-" in text:
            try:
                result = int(first_char) - int(last_char)
            except ValueError:
                result = False
        if "*" in text:
            try:
                result = int(first_char) * int(last_char)
            except ValueError:
                result = False
        if "/" in text:
            try:
                result = int(first_char) / int(last_char)
            except ValueError:
                result = False
    else:
        getCaptcha = get_captcha('http://127.0.0.1/dev-api/captchaImage').json()
        decode_base64_to_img(getCaptcha['img'])
        verification()
    if not result:
        getCaptcha = get_captcha('http://127.0.0.1/dev-api/captchaImage').json()
        decode_base64_to_img(getCaptcha['img'])
        verification()
    data = {
        "code": result,
        "uuid": getCaptcha['uuid']
    }
    return data
