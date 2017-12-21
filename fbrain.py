from flask import Flask, render_template
from config import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/csv/<int:head>:<int:tail>')
@app.route('/csv/<int:head>:<int:tail>:<int:scale>')
def csv(head=0, tail=-0, scale=1):
    return # folan


from uart import start_provide
start_provide()

app.run(debug=True)