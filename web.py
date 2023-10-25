from flask import Flask, render_template, request

from datetime import datetime

app = Flask(__name__)

@app.route("/")

def index(): 

	x = "作者：徐维骏<br>"

	x +="<a href=/mis>课程</a><br>"

	x +="<a href=/Skhsu?nick=Ivvin>个人</a><br>"

	x +="<a href=/account>表单</a><br>"

	return x

@app.route("/mis")

def course():

	return "<a href='https://drive.google.com/drive/folders/1JGHLQWpzT2QxSVPUwLxrIdYowijWy4h1'><h1>資訊管理導論</h1></a>"

@app.route("/Skhsu",methods=["GET", "POST"])

def Skhsu():

	now = str(datetime.now())

	user = request.values.get("nick")

	return render_template("Skhsu.html",datetime=now, name=user)

@app.route("/account", methods=["GET", "POST"])

def account():

	if request.method == "POST":

		user = request.form["user"]

		pwd = request.form["pwd"]

		result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd

		return result

	else:

		return render_template("account.html")

if __name__ == "__main__":

	app.run()