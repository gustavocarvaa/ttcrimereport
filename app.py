import os
from flask import Flask, render_template



app = Flask(__name__)

app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/home')
def Home():
    return render_template('home.html', title='Início')


@app.route('/about')
def About():
    return render_template('about.html', title='Sobre')


@app.route('/layout')
def Layout():
    return render_template('layout.html', title='')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)