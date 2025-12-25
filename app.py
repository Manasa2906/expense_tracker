from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("expenses.db")

@app.route("/")
def index():
    db = get_db()
    expenses = db.execute("SELECT * FROM expenses").fetchall()
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form["amount"]
    category = request.form["category"]
    note = request.form["note"]

    db = get_db()
    db.execute(
        "INSERT INTO expenses (amount, category, note) VALUES (?, ?, ?)",
        (amount, category, note)
    )
    db.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
