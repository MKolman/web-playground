from flask import Flask, render_template, request, make_response, session, redirect

import devel
import broken

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/logout")
def logout():
    if "user" in session:
        del session["user"]
    return redirect("/login")


app.add_url_rule("/reset_db", 'reset_db', devel.reset_db)
app.add_url_rule("/login", 'login', broken.login)
app.add_url_rule("/bad_search", 'bad_search', broken.bad_search)
app.add_url_rule("/evil", 'evil', broken.evil)
app.add_url_rule("/forum", 'forum', broken.forum)
app.secret_key = 'password'
app.config.update(SESSION_COOKIE_HTTPONLY=False)

if __name__ == "__main__":
    app.run()
