import traceback
import uuid
import sqlite3

from flask import Flask, render_template, request, make_response, session, redirect, abort

import devel
import broken
from settings import DB_NAME

application = Flask(__name__)
application.debug = False

if 0:
    @application.before_request
    def csrf_protect():
        if request.method == "POST":
            token = session.get('_csrf_token', None)
            print(token == request.form.get('_csrf_token'))
            print(repr(token), repr(request.form.get('_csrf_token')))
            if not token or token != request.form.get('_csrf_token'):
                abort(403)

    def generate_csrf_token():
        if '_csrf_token' not in session:
            session['_csrf_token'] = str(uuid.uuid4())
        print(session['_csrf_token'])
        return session['_csrf_token']

    application.jinja_env.globals['csrf_token'] = generate_csrf_token


@application.before_request
def set_user():
    if "user" in session:
        username = session.get("user")[1]
        conn = sqlite3.connect(DB_NAME)
        user = next(conn.execute("SELECT * FROM users WHERE username=?", (username, )))
        conn.close()
        session["user"] = user


@application.errorhandler(500)
def internal_error(exception):
    """Show traceback in the browser when running a flask app on a production server.
    By default, flask does not show any useful information when running on a production server.
    By adding this view, we output the Python traceback to the error 500 page.
    """
    trace = traceback.format_exc()
    return("<pre>" + trace + "</pre>"), 200


@application.route("/")
def root():
    return render_template("index.html")


@application.route("/logout")
def logout():
    if "user" in session:
        del session["user"]
    return redirect("/login")


application.add_url_rule("/reset_db", 'reset_db', devel.reset_db, methods=["GET", "POST"])
application.add_url_rule("/pay", 'pay', broken.pay, methods=["GET", "POST"])
application.add_url_rule("/login", 'login', broken.login, methods=["GET", "POST"])
application.add_url_rule("/search", 'search', broken.search)
application.add_url_rule("/forum", 'forum', broken.forum, methods=["GET", "POST"])
application.add_url_rule("/db_viewer_XDSie983BQbnxc_asjdh", 'db_view', broken.db_view)
application.add_url_rule("/evil", 'evil', broken.evil)
application.add_url_rule("/evil_bun", 'evil_bun', broken.evil_bun)
application.secret_key = 'password'
application.config.update(SESSION_COOKIE_HTTPONLY=False, DEBUG=False)
# application.DEBUG = False
# application.debug = False

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=False)
