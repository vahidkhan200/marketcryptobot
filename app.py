from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route("/")
def home():
    if os.path.exists("signals.json"):
        with open("signals.json", "r") as f:
            data = json.load(f)
    else:
        data = []
    return render_template("index.html", signals=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
