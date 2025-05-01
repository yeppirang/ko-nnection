from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

with open("words.json", encoding="utf-8") as f:
    data = json.load(f)
    all_words = sum(data["groups"], [])

@app.route("/")
def index():
    return render_template("index.html", words=all_words)

@app.route("/check", methods=["POST"])
def check():
    selected = request.json.get("words", [])
    selected_set = set(selected)
    for group in data["groups"]:
        if selected_set == set(group):
            return jsonify({"result": "정답입니다!"})
    return jsonify({"result": "틀렸습니다."})

if __name__ == "__main__":
    # Render가 요구하는 포트로 바인딩
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
