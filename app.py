from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    submitted = request.args.get("submitted")
    return render_template("index.html", submitted=submitted)

@app.route("/submit", methods=["POST"])
def submit():
    report_text = request.form.get("report")
    print(report_text)  #temporary, for learning

    return redirect(url_for("home", submitted="true"))

if __name__ == "__main__":
    app.run(debug=True)