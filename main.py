from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start.html')
@app.route("/question_1")
def question_1():
    return render_template("question_1.html")

@app.route("/question_1/final")
def final():
    return render_template("final.html")
app.run(debug=True)