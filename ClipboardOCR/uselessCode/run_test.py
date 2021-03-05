import base64
from PIL import Image
from PIL import ImageGrab
# import pyperclip
from io import BytesIO

def pil_base64(image):
    img_buffer = BytesIO()
    w, h = image.size
    # image.thumbnail((128, 128))
    image.save(img_buffer, format='JPEG', quality=95)
    byte_data = img_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str

im = ImageGrab.grabclipboard()

if isinstance(im, Image.Image):

    px_rgb = im.convert("RGB")
    msg = str(pil_base64(px_rgb))
    msg1 = 'data:image/png;base64,' + msg[2:-2]
    print(msg1)

else:
    pass

# ————————————————
# 版权声明：本文为CSDN博主「verse_monger」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/verse_monger/article/details/105899925