from flask import Flask, render_template, redirect, request
import flask
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/github")
def github():
	return render_template("github.html")
	
@app.route("/mail")
def mail():
	return render_template("mail.html")
	
@app.route("/medium")
def medium():
	return render_template("medium.html")
	
@app.route("/discord")
def discord():
	return render_template("discord.html")

@app.route("/reddit")
def reddit():
	return render_template("reddit.html")
	
@app.route("/youtube")
def youtube():
	return render_template("youtube.html")

if __name__ == "__main__":
	app.run(debug=True)