# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import simulator
import requests

app = Flask(__name__)

url = "https://api.heroku.com/apps/revolving-credit-simulation/config-vars"
headers = {"Accept": "application/vnd.heroku+json; version=3"}
response = requests.get(url, headers=headers).json()

# app.config["KEEN_PROJECT_ID"] = response["KEEN_PROJECT_ID"]
# app.config["KEEN_WRITE_KEY"] = response["KEEN_WRITE_KEY"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    borrowing = request.form.get("borrowing", type=int)
    repayment = request.form.get("repayment", type=int)
    if borrowing is None or repayment is None:
        return render_template("error.html", error=response)
    else:
        result, result_list = simulator.simulate(borrowing, repayment)
        return render_template("result.html", result=result, result_list=result_list)

if __name__ == "__main__":
    app.run(debug=True)
