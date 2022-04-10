from flask import Flask, render_template, redirect, request, make_response
import flask
app = Flask(__name__,template_folder="./templates")

@app.route("/")
def home():
	return render_template("index.html")
	
<<<<<<< HEAD
if __name__ == "__main__":
	app.run(debug=True)
=======
@app.route("/mail")
def mail():
	return render_template("mail.html")
	
@app.route("/discord")
def discord():
	return render_template("discord.html")
	
@app.route("/youtube")
def youtube():
	return render_template("youtube.html")

app.run(debug=True)
>>>>>>> refs/remotes/origin/main
