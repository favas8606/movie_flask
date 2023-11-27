from flask import Flask
app = Flask(__name__)


@app.route('/')

def home():
    return '<h1>Hello world </h1>'



@app.route('/new')

def new():
    return '<center><h1>Welcome to Flask programming</h1></center>'

app.run()