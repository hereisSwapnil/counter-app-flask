from flask import Flask, render_template, render_template_string


app = Flask(__name__, template_folder='static')

database = {"number" : 0}

@app.route('/')
def hello():
    return render_template("home_page.html",number = database["number"])

@app.route('/decrement')
def decrement():
    database["number"] -= 1
    return render_template("home_page.html",number = database["number"])

@app.route('/increment')
def increment():
    database["number"] += 1
    return render_template("home_page.html",number = database["number"])

app.run(host="0.0.0.0", port=5000)