import base64
from PIL import Image


def decode_base64_to_img(base64_str):
    img_data = base64.b64decode(base64_str)
    with open('image.jpg', 'wb') as f:
        f.write(img_data)
    f.close()

