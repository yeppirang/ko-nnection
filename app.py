from flask import Flask, render_template, request, jsonify
import json
import os
import random

app = Flask(__name__)

with open("words.json", encoding="utf-8") as f:
    data = json.load(f)
    groups = data["groups"]
    all_words = sum([g["words"] for g in groups], [])

@app.route("/")
def index():
    shuffled = all_words[:]
    random.shuffle(shuffled)
    return render_template("index.html", words=shuffled)

@app.route("/check", methods=["POST"])
def check():
    selected = request.json.get("words", [])
    selected_set = set(selected)

    for group in data["groups"]:
        if selected_set == set(group["words"]):
            return jsonify({
                "result": "정답입니다!", 
                "category": group["category"], 
                "color": group.get("color", "#ffd700")
                })
    return jsonify({"result": "틀렸습니다."})

if __name__ == "__main__":
    # Render가 요구하는 포트로 바인딩
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
