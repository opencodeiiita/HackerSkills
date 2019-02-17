from flask import Flask,Response
import json
import random 
app=Flask(__name__)

quotes = [{
	"book": "Harry Potter and the Philosopher's Stone",
	"quote": "It does not do to dwell on dreams and forget to live."},
{
	"book": "Harry Potter and the Half Blood Prince",
	"quote": "And now, Harry, let us step out into the night and pursue that flighty temptress, adventure."},
{
	"book": "Harry Potter and the Goblet of Fire",
	"quote": "Differences of habit and language are nothing at all if our aims are identical and our hearts are open."},
{
	"book": "Harry Potter and the Goblet of Fire",
	"quote": "Numbing the pain for a while will make it worse when you finally feel it."},
{
	"book": "Harry Potter and the Chamber of Secrets",
	"quote": "Mater gave Dobby a sock! Dobby is freeeee!"},
{
	"book": "Harry Potter and the Prisoner of Azkaban",
	"quote": "The ones that love us never really leave us. They always are in here."},
{
	"book": "Harry Potter and the Order of Phoenix",
	"quote": "Things we lose have a way of coming back to us in the end, if not always in the way we expect."},
{
	"book": "Harry Potter and the Deathly Hallows",
	"quote": "Until the very end."},
]



@app.route('/quotes', methods=['GET'])
def get_quote():
	x = Response(json.dumps(quotes))
	return x

@app.route('/quote/random', methods=['GET'])
def get_random_quote():
	length = random.randint(0,len(quotes))
	x= Response(json.dumps(quotes[length]))
	return x

if __name__=='__main__':
	app.run(debug=True)
