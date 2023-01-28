from flask import Flask
from scrape import *

app = Flask(__name__)

<<<<<<< HEAD
'''
=======
>>>>>>> 6eec9bec81fad1fcd0c5ffe6d0d49b2a969d187e
@app.route('/')
def print_results():
    return get_results()
'''

<<<<<<< HEAD
@app.route('/')
def home():
    return render_template('index.html')

=======
>>>>>>> 6eec9bec81fad1fcd0c5ffe6d0d49b2a969d187e
@app.route('/route_name')
def script_output():
    output = execute('./script')
    return render_template('./../templates/index.html', output=output)

if __name__ == '__main__':
    app.run()
