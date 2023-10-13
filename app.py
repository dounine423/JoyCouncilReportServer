from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
app.debug = True

CORS(app)

@app.route('/' , methods = ['GET','POST'])
def index():
    return 'joy stream council reprot server is running'

@app.route('/getStorage',methods=['POST'])
def getStorageFunc():
    return 'result'

@app.route('/getNonEmptyChannel',methods=['POST'])
def getNonEmptyChannelFunc():
    return 'result'


if __name__ == "__main__":
    # app.run(ssl_context='adhoc',host="0.0.0.0",port=5000,debug=True)
    app.run(host="0.0.0.0",port=5000,debug=True)


