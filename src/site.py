from flask import Flask
from scrape import *

app = Flask(__name__)

@app.route('/')
def print_results():
    return get_results()

@app.route('/route_name')
def script_output():
    output = execute('./script')
    return render_template('index.html',output=output)

if __name__ == '__main__':
    app.run()
