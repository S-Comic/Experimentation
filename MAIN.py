from flask import render_template, Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/writing/')
def writing():
    return render_template('writing.html')

@app.route('/coding/')
def coding():
    return render_template('coding.html')
