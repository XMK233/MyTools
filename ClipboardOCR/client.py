import requests
import json
import base64
from io import BytesIO
from PIL import Image
from PIL import ImageGrab
import time
import pyperclip
# from ctypes import windll

def pil_base64(image):
    img_buffer = BytesIO()
    w, h = image.size
    image.save(img_buffer, format='JPEG', quality=95)
    byte_data = img_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str
print("Started. Now just shoot the screen.\n\n\n")
while True:
    time.sleep(1)

    im = ImageGrab.grabclipboard()

    if isinstance(im, Image.Image):
        px_rgb = im.convert("RGB")
        msg = str(pil_base64(px_rgb))
        encode = msg[2:-1]
        # 发送HTTP请求
        data = {'images': [
            encode
        ]}
        headers = {"Content-type": "application/json"}
        url = "http://127.0.0.1:8866/predict/chinese_ocr_db_crnn_mobile"
        r = requests.post(url=url, headers=headers, data=json.dumps(data))
        # 打印预测结果
        res = []
        for item in r.json()["results"][0]["data"]:
            text = item["text"]
            text_new = text.replace("（", "(").replace("）", ")")
            # print(text_new)
            res.append(text_new)
        output_str = "\n".join(res)
        pyperclip.copy(output_str)
        print(output_str)
        print()
    else:
        pass

# https://blog.csdn.net/verse_monger/article/details/105899925
# https://www.thinbug.com/q/579687
# https://www.paddlepaddle.org.cn/hubdetail?name=chinese_ocr_db_crnn_mobile&en_category=TextRecognition