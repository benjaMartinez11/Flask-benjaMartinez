from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/Yo')
def Yo():
    return '💛💙BOCA BOCA BOCA💛💙'