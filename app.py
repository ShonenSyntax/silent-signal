from flask import Flask, render_template, request, jsonify, redirect, url_for
from ai_utils import analyze_report

app = Flask(__name__)

@app.route("/")
def home():
    submitted = request.args.get("submitted")
    return render_template("index.html", submitted=submitted)

@app.route("/submit", methods=["POST"])
def submit():
    report_text = request.form.get("report")

    analysis = analyze_report(report_text)

    print("\nRAW REPORT: ")
    print(report_text)

    print("\nAI ANALYSIS: ")
    print(analysis)

    return redirect(url_for("home", submitted="true"))

if __name__ == "__main__":
    app.run(debug=True)