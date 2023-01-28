from flask import Flask
from flask import render_template
from main import *

app = Flask(__name__)

@app.route('/')
def home():
    # return results
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
