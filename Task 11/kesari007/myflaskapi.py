from flask import Flask, jsonify
import numpy as np
import json

app = Flask(__name__)
with open('myquotes.json') as my_file : 
	quote_data = json.load(my_file)
	my_file.close()
quotes = quote_data['quotes']

@app.route('/')
def index():
	return jsonify({"Hello":"world"})

@app.route('/quotes',methods= ['GET'])
def get_quote():
	return jsonify({'quote' : quotes})

@app.route('/rand',methods = ['GET'])
def get_rand_quote():
	x = np.random.randint(0,len(quotes))
	return jsonify({'quote': quotes[x]})


if __name__=='__main__':
	app.run(debug=True)