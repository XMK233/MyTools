import requests
import json
import base64
from io import BytesIO
from PIL import Image
from PIL import ImageGrab
import time
import pyperclip
import os

path = r"C:\Users\XMK23\Pictures"

fileNum = 8
# numOfPicture = 21

def getBase64(imgNum):
    res = None
    with open(os.path.join(path, "Picture{}.png".format(imgNum)), "rb") as f:
        base64_data = base64.b64encode(f.read())
        res = "data:image/png;base64,{}".format(base64_data.decode('utf-8'))
    return res

with open("{}.html".format(fileNum), "w", encoding="utf-8") as h:

    headPart = """
    <!DOCTYPE html>  
    <html>  
    <head>  
        <title>Section {}</title>  
        <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">  
        <meta http-equiv="description" content="this is my page">  
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">  
    </head>  
    <body> 


    """.format(fileNum)
    h.write(headPart)
    ######################################
    # counter = 0
    # for counter in range(1, numOfPicture + 1):
    #     with open(os.path.join(path, "Picture{}.png".format(counter)), "rb") as f:
    #         base64_data = base64.b64encode(f.read())
    #         h.write("<img id = {} src = data:image/png;base64,{}>\n\n\n".format(counter, base64_data.decode('utf-8')))
    #############################
    h.write('<font color="red" size="5">第一段落: </font><br>\n\n')
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(1, getBase64(1)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(2, getBase64(2)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(3, getBase64(3)))    
    h.write("(上两图，一手不贴杠)\n")
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(4, getBase64(4)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(5, getBase64(5)))
    h.write("(上图，右手打右杠)\n")
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(6, getBase64(6)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(7, getBase64(7)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(8, getBase64(8)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(9, getBase64(9)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(10, getBase64(10)))
    # h.write('<font color="red" size="5">第三段落: </font><br>\n\n')
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(11, getBase64(11)))
    
    h.write('<br><font color="red" size="5">第二段落: </font><br>\n\n')
    # h.write("(上图，看样子，右腿要顶底杠)\n")
    # h.write("(上图，打击左杠)\n")
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(12, getBase64(12)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(13, getBase64(13)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(14, getBase64(14)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(15, getBase64(15)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(16, getBase64(16)))
    ####################################
    h.write('<br><font color="red" size="5">第三段落: </font><br>\n\n')
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(17, getBase64(17)))
    h.write("(上图，右手是贴着左杠)\n")
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(18, getBase64(18)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(19, getBase64(19)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(20, getBase64(20)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(21, getBase64(21)))
    h.write("(上图，右手按中杠)\n")
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(22, getBase64(22)))
    h.write("(拍上横杠, 左手先拍, 右手后拍)\n")
    ##############################
    h.write('<br><font color="red" size="5">第四段落: </font><br>\n\n')
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(23, getBase64(23)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(24, getBase64(24)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(25, getBase64(25)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(26, getBase64(26)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(27, getBase64(27)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(28, getBase64(28)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(29, getBase64(29)))
    #####################
    h.write('<br><font color="red" size="5">第五段落: </font><br>\n\n')
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(30, getBase64(30)))
    h.write("(上图，左腿扣底杠)\n")
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(31, getBase64(31)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(31, getBase64(32)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(31, getBase64(33)))
    h.write("<img id = {} width = 155 src = {}>\n\n\n".format(31, getBase64(34)))
    ########################
    h.write('<br><font color="red" size="5">完结撒花. </font><br>\n\n')
    # 
    
    # h.write("<br>\n")
    
    ###############################
    
    # 
    
    # h.write("<img id = {} width = 155 src = {}>\n\n\n".format(30, getBase64(30)))
    # h.write("<img id = {} width = 155 src = {}>\n\n\n".format(31, getBase64(31)))
    # h.write("<br>\n")
    # h.write("**前面图, 有误. 不是右手横击而是左手横击. ")
    ###########################
    tailPart = """




        </body>  
    </html> 
    """
    h.write(tailPart)