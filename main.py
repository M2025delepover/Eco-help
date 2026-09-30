from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start.html')
@app.route("/question_<int:n>")
def question(n):
    return render_template(f"question_{n}.html")

@app.route("/final")
def final():
    return render_template("final.html")
app.run(debug=True)