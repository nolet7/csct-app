from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    try:
        conn = mysql.connector.connect(
            host="192.168.0.169",
            user=os.environ.get("MYSQL_USERNAME"),
            password=os.environ.get("MYSQL_PASSWORD"),
            database="csct_db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, status FROM components")
        components = cursor.fetchall()
        return render_template("dashboard.html", components=components)
    except Exception as e:
        return f"<h2>Failed to load data: {e}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
