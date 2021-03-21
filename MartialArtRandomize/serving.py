from flask import Flask
from GenerateList import consume_list
from flask import render_template, request

app = Flask(__name__, template_folder="IpMan_Murenzhuang")

@app.route('/')
def hello_world():
    return 'Hello, Martial Art World!'

@app.route('/next')
def nextMartialArt():
    return consume_list()

@app.route('/yongchun', methods = ['GET'])
def getPage():
    page = request.args.get("p")
    return render_template("{}.html".format(page)) 

if __name__ =="__main__":
    app.run(debug=True,port=54233)