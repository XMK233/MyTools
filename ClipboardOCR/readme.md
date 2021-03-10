### Step 1: run the code `client.py` in win cmd

Conda env on my computer: `tf2`

Need to install `pyperclip, Pillow` in advance. 

Run the `startClient.bat` to start the client. 

### Step 2: start the server with ubuntu shell: 

Remember, use Ubuntu (WSL), never use Windows, which is totally a tragedy.

Conda env on my computer: `base`

Go to [this page](https://www.paddlepaddle.org.cn/hubdetail?name=chinese_ocr_db_crnn_mobile&en_category=TextRecognition) to get information for installing libraries`paddle (2.0.0+), paddlehub (2.0.0+), shapely, pyclipper`. 

Open a WSL shell at the current directory, then run 

```shell
$ sh serveTheOCRModel.sh
```

to serve the OCR model. 

Remember, you have to wait for a while to let the model finish serving. Don't hush to do the following step. 

### Step 3: capture the screen

Then you can just use the windows snip tool to capture the screen. After waiting for a while, the OCR result will be automatically stored in clipboard, and you can also see the OCR result shown in cmd window. 

