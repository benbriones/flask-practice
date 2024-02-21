from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def say_welcome():
    """returns string welcome"""
    return 'welcome'

@app.get('/welcome/home')
def say_welcome_home():
    """returns string welcome home"""
    return "welcome home"


@app.get('/welcome/back')
def say_welcome_back():
    """returns string welcome back"""
    return "welcome back"
