from flask import Flask, jsonify, render_template
app = Flask(__name__)

import os

@app.route('/')
def hello_world():
    return 'Hello'


@app.route('/api/')
@app.route('/api/<dir>')
def ls(dir='.'):
    files = os.listdir(dir)
    return render_template('layout.html',files=files)


if __name__ == '__main__':
    app.run(debug=True)
