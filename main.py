from flask import Flask, render_template, request, make_response, session, redirect

import devel
import broken

application = Flask(__name__)


@application.route("/")
def root():
    return render_template("index.html")


@application.route("/logout")
def logout():
    if "user" in session:
        del session["user"]
    return redirect("/login")


application.add_url_rule("/reset_db", 'reset_db', devel.reset_db)
application.add_url_rule("/login", 'login', broken.login)
application.add_url_rule("/bad_search", 'bad_search', broken.bad_search)
application.add_url_rule("/evil", 'evil', broken.evil)
application.add_url_rule("/forum", 'forum', broken.forum)
application.add_url_rule("/db_viewer_XDSie983BQbnxc_asjdh", 'db_view', broken.db_view)
application.secret_key = 'password'
application.config.update(SESSION_COOKIE_HTTPONLY=False, DEBUG=True)
application.DEBUG = True
application.debug = True

if __name__ == "__main__":
    application.run()
