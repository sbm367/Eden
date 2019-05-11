'''
import os
import pandas as pd
import nltk
'''
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Deployed to Heroku!</h1>'

if __name__=='__main__':
	app.run(debug=True)
	
#print("this is only a test uwu")

#nltk.download()