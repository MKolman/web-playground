import traceback
from flask import Flask, render_template, request, make_response, session, redirect

import devel
import broken

application = Flask(__name__)
application.debug = False


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
application.add_url_rule("/login", 'login', broken.login, methods=["GET", "POST"])
application.add_url_rule("/search", 'search', broken.search)
application.add_url_rule("/evil", 'evil', broken.evil)
application.add_url_rule("/forum", 'forum', broken.forum, methods=["GET", "POST"])
application.add_url_rule("/db_viewer_XDSie983BQbnxc_asjdh", 'db_view', broken.db_view)
application.secret_key = 'password'
application.config.update(SESSION_COOKIE_HTTPONLY=False, DEBUG=False)
# application.DEBUG = False
# application.debug = False

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=False)
