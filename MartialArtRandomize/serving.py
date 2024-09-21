from flask import Flask
from GenerateList import consume_list
from flask import render_template, request

app = Flask(__name__) ## , template_folder="IpMan_Murenzhuang"

@app.route('/')
def hello_world():
    return render_template("welcome.html")  ## 'Hello, Martial Art World!'

@app.route('/next')
def nextMartialArt():
    ma = consume_list()
    return render_template("display.html", ma = ma)

@app.route('/yongchun', methods = ['GET'])
def getPage_yongchun():
    page = request.args.get("p")
    return render_template("IpMan_Murenzhuang/{}.html".format(page)) 

@app.route('/sjg', methods = ['GET'])
def getPage_sjg():
    page = request.args.get("p")
    return render_template("shuang_jie_gun_18/{}.html".format(page)) 

# ##########
# @app.route('/json')
# def json():
#     return render_template('welcome.html')

# ##background process happening without any refreshing
# @app.route('/background_process_test')
# def background_process_test():
#     print ("Hello")
#     return "nothing"

if __name__ =="__main__":
    app.run(debug=True,port=54233)