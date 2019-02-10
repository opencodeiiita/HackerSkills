from flask import Flask,Response

import json
import random
app=Flask(__name__)

quotes = [{
	"author": "Abraham Lincoln",
	"quote": "Things may come to those who wait, but only the things left by those who hustle."},
{
	"author": "Adam Smith",
	"quote": "The great secret of education is to direct vanity to proper objects."},
{
	"author": "Alain de Botton",
	"quote": "It’s not that travel just broadens your mind, rather it enables you to see how narrow your oppressor’s minds are."},
{
	"author": "Alan Watts",
	"quote": "A person who never made a mistake never tried anything new."},
{
	"author": "Alan Watts",
	"quote": "Better to have a short life that is full of what you like doing than a long life spent in a miserable way."},
{
	"author": "Alan Watts",
	"quote": "Life is a musical thing and you are supposed to dance and sign while it's being played."},
{
	"author": "Alan Watts",
	"quote": "Omnipotence is not knowing how everything is done; it's just doing it."},
{
	"author": "Albert Camus",
	"quote": "It is not humiliating to be unhappy. Physical suffering is sometimes humiliating, but the suffering of being cannot be, it is life."},
{
	"author": "Albert Einstein",
	"quote": "The secret to creativity is knowing how to hide your sources."},
{
	"author": "Albert Einstein",
	"quote": "The true sign of intelligence is not knowledge but imagination."},
]



@app.route('/quotes')
def quote():
	response = Response(
	json.dumps(quotes[rand]), status=200)
	return response

@app.route('/quote/random')
def quote_random():
	rand = random.randint(0,len(quotes))
	response= Response(
	json.dumps(quotes[rand], status=200)
	return response

if __name__=='__main__':
	app.run(debug=True)

if __name__=='__main__':
	app.run(debug=True)