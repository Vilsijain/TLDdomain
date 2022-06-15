import os
import random
from flask import Flask,jsonify


app = Flask(__name__)

@app.route('/<string:words>')
def append(words):
    result=[]
    str2 = ['.com',  '.net', '.org', '.Whois Privacy']
    for i in random.sample(str2,4):
        strres=words+i
        result.append(strres)
    return jsonify(result)
if __name__ == '__main__':
    port = os.getenv('PORT',None) or 80
    app.run(host='0.0.0.0',port=port,debug=True)
