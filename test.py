from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/second')
def second():
    return render_template('second.html')


app.run(port=5000, debug=True)
