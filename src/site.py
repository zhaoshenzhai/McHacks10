from flask import Flask
from main import *

app = Flask(__name__)

@app.route('/')
def home():
    return results

if __name__ == '__main__':
    app.run()
