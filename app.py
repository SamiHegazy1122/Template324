from flask import Flask, render_template, request, redirect, url_for
import helper

app = Flask(__name__)


@app.route("/")
def index():
    items = helper.get_all()
    return render_template("index.html", items=items)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")
    date = request.form.get("date")
    if date:
        helper.add(text, date)
    else:
        helper.add(text)
    return redirect(url_for("index"))


@app.route("/update/<int:index>", methods=["POST"])
def update(index):
    helper.update(index)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
