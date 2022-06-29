from flask import Flask, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test1')
def test_1():
    return "apple"

@app.route('/test2')
def test_2():
    return "orange"