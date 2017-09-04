# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import simulator
import requests
import os

app = Flask(__name__)

if os.environ.get("KEEN_PROJECT_ID") is not None and os.environ.get("KEEN_WRITE_KEY") is not None:
    app.config["DEBUG"] = False
    app.config["KEEN_PROJECT_ID"] = os.environ["KEEN_PROJECT_ID"]
    app.config["KEEN_WRITE_KEY"] = os.environ["KEEN_WRITE_KEY"]
else:
    app.config["DEBUG"] = True

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
