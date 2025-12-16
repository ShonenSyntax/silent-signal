from flask import Flask, render_template, request, jsonify, redirect, url_for
from ai_utils import analyze_report, parse_analysis
from db import db
from datetime import datetime
from db_utils import get_all_reports

app = Flask(__name__)

@app.route("/")
def home():
    submitted = request.args.get("submitted")
    return render_template("index.html", submitted=submitted)

@app.route("/submit", methods=["POST"])
def submit():
    report_text = request.form.get("report")

    #Ai Analysis
    analysis_text = analyze_report(report_text)
    parsed = parse_analysis(analysis_text)

    #Firestore Document
    report_data = {
        "report_text": report_text,
        "summary": parsed["summary"],
        "category": parsed["category"],
        "severity": parsed["severity"],
        "timestamp": datetime.utcnow()
    }

    #Save to Firestore
    db.collection("reports").add(report_data)

    return redirect(url_for("home", submitted="true"))

@app.route("/admin")
def admin():
    reports = get_all_reports()
    return render_template("admin.html", reports = reports)

if __name__ == "__main__":
    app.run(debug=True)