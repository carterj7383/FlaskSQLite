from flask import Flask, render_template
import sqlite3

app = Flask(__name__, static_url_path="/templates")

@app.route("/people")
def people():
    con = sqlite3.connect("people.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM People;")
    people = cur.fetchall()
    return render_template("people.html", people=people)

@app.route("/")
def index():
    return render_template("index.html")