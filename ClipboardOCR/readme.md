### Step 1: start the server with ubuntu shell: 

Remember, use Ubuntu, never use Windows, which is totally a tragedy.

Conda env on my computer: `base`

Go [this page](https://www.paddlepaddle.org.cn/hubdetail?name=chinese_ocr_db_crnn_mobile&en_category=TextRecognition), 
to install paddle (2.0.0+), paddlehub (2.0.0+), shapely, pyclipper.  

Run the command to serve the model. 

    $ hub serving start -m chinese_ocr_db_crnn_mobile

### Step 2: run the code `client.py` in win cmd

Conda env on my computer: `tf2`

Need to install `pyperclip, Pillow`

Then you can just use the windows snip tool to shoot the screen. 
The OCR result will be automatically stored in clipboard, and you can 
also see the OCR result output in cmd. 

