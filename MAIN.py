from flask import render_template, Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def hello():
    return render_template('login.html')

@app.route('/navigation/')
def navi():
    return render_template('navigation.html')
