from flask import Flask, render_template, request, make_response

import devel
import broken

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/evil")
def evil():
    return render_template("evil.html")


app.add_url_rule("/reset_db", 'reset_db', devel.reset_db)
app.add_url_rule("/bad_search", 'bad_search', broken.bad_search)
app.add_url_rule("/forum", 'forum', broken.forum)

if __name__ == "__main__":
    app.run()
