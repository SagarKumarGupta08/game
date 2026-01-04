from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save-score", methods=["POST"])
def save_score():
    score = request.json["score"]
    with open("scores.txt", "a") as f:
        f.write(str(score) + "\n")
    return jsonify({"status": "saved"})

if __name__ == "__main__":
    app.run(debug=True)
