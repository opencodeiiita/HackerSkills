#!flask/bin/python
from flask import Flask,request,jsonify

app = Flask(__name__)

quote = [
    {
        "author": "Edgar Rice Burroughs",
        "description": "A vivid and blinding light flashed from the whirling, inky clouds above. The deep cannonade of roaring thunder belched forth its fearsome challenge. The deluge came--all hell broke loose upon the jungle"
    },
    {
        "author": "Emily Bronte",
        "description": "I gave him my heart, and he took and pinched it to death, and flung it back to me"
    },
    {
        "author": "H. Rider Haggard",
        "description": "Who has not in his great grief felt a longing to look upon the outward features of the universal Mother; to lie on the mountains and watch the clouds drive across the sky and hear the rollers break in thunder on the shore, to let his poor struggling life mingle for a while in her life; to feel the slow beat of her eternal heart, and to forget his woes"
    },
    {
        "author": "Mark Twain",
        "description": "All I say is, kings is kings, and you got to make allowances. Take them all around, they're a mighty ornery lot. It's the way they're raised."
    },
    {
        "author": "Charles Dickens",
        "description": "Annual income twenty pounds, annual expenditure nineteen nineteen and six, result happiness. Annual income twenty pounds, annual expenditure twenty pounds ought and six, result misery."
    },
    {
        "author": "Emily Bronte",
        "description": "I gave him my heart, and he took and pinched it to death, and flung it back to me"
    }
]

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/quote', methods=['GET'])
def get_tasks():
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(debug=True)
