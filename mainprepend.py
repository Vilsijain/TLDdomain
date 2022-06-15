import os
import random
from flask import Flask,jsonify


app = Flask(__name__)

@app.route('/<string:words>')
def prepend(words):
    result=[]
    str2 = ['ve', 'bright', 'toffee', 'code', 'community', 'dev', 'eat', 'drink', 'repeat']
    for i in random.sample(str2,5):
        strfin=i+words
        result.prepend(strfin) 
    return jsonify(result)
if __name__ == '__main__':
    port = os.getenv('PORT',None) or 80
    app.run(host='0.0.0.0',port=port,debug=True)