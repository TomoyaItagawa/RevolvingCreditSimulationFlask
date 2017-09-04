# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import simulator

app = Flask(__name__)
app.config.from_object("config")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    borrowing = request.form.get("borrowing", type=int)
    repayment = request.form.get("repayment", type=int)
    if borrowing is None or repayment is None:
        return render_template("error.html", error="入力欄に数字を入力してください。")
    else:
        result, result_list = simulator.simulate(borrowing, repayment)
        return render_template("result.html", result=result, result_list=result_list)

if __name__ == "__main__":
    app.run(debug=True)
