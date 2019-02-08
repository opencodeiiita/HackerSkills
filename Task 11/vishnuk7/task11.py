from flask import Flask,Response
import json
from random import randint
app = Flask(__name__)

with open('./data.json', 'r',encoding="utf8") as myfile:
    data = json.loads(myfile.read())



@app.route("/quote")
def quote():
    response = Response(
        json.dumps(data),status =200)
    return response
    
@app.route("/quote/random")
def quoteRandom():
    rand = randint(0, len(data["quotes"]))
    response = Response(
        json.dumps(data["quotes"][rand]),status =200)
    return response

if __name__ == '__main__':
    app.run(debug=True)