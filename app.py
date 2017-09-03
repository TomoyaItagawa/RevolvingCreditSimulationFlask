# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import simulator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    borrowing = int(request.form["borrowing"])
    repayment = int(request.form["repayment"])
    result, result_list = simulator.simulate(borrowing, repayment)
    return render_template("result.html", result=result, result_list=result_list)

if __name__ == "__main__":
    app.run(debug=True)
