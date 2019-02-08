#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
from random import randint
from flask.ext.cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('quotes.json') as data_file:    
    data = json.load(data_file)
    data_file.close()
quotes = data['quotes']    

    
@app.route('/')
def index():
    return 'Hello! How are you??'


@app.route('/quotes/api/random', methods=['GET'])
def get_quote_random():
    q_id=randint(0,len(quotes)-1)
    return jsonify({'quotes': quotes[q_id]})
    
    
    
@app.route('/quotes/api/quote/<int:quote_id>', methods=['GET'])
def get_quote_id(quote_id):
    quote = [quote for quote in quotes if quote['id'] == quote_id]
    if len(quote) == 0:
        abort(404)
    return jsonify({'quotes': quote})

    
    
@app.route('/quotes/api/quote/<author>', methods=['GET'])
def get_quote_author(author):
    quote = [quote for quote in quotes if quote['author'] == author]
    if len(quote) == 0:
        abort(404)
    return jsonify({'quotes': quote})

    

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'quotes':{'id': u'error','quote': u'error','author': u'error'}}), 404)

    
      
if __name__ == '__main__':
    app.run(debug==True)
