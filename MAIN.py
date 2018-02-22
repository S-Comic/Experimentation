from flask import render_template, Flask
app = Flask(__name__)

@app.route('/hello/')
def hello():
    return render_template('hello.html')

@app.route('/navigation/')
def navi():
    return render_template('navigation.html')

@app.route('/')
def index():
    return render_template('index.html')
