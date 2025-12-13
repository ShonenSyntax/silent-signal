from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    report_text = request.form.get("report")
    print(report_text)  #temporary, for learning

    return "Report received anonymously"

if __name__ == "__main__":
    app.run(debug=True)