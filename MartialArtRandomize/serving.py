from flask import Flask
from GenerateList import consume_list

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Martial Art World!'

@app.route('/next')
def nextMartialArt():
    return consume_list()

if __name__ =="__main__":
    app.run(debug=True,port=54233)