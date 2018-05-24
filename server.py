from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def landing_page():
    return render_template('index.html')

@app.route('/ninjas')

def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')

def new_dojos():
    return render_template('dojos.html')

app.run(debug=True)