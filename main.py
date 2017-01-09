from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def root():
    search = request.args.get("search")
    return render_template("bad_search.html", search=search)


@app.route("/bad_search")
def bad_search():
    search = request.args.get("search")
    return render_template("bad_search.html", search=search)


if __name__ == "__main__":
    app.run()
