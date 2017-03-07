import sqlite3

from flask import render_template, request, make_response

from settings import DB_NAME


def bad_search():
    search = request.args.get("search")
    results = []

    conn = sqlite3.connect(DB_NAME)
    if search:
        for word in search.split(" ", 1):
            results += conn.execute("""
                SELECT * FROM links WHERE lower(desc) LIKE '{0}'
                """.format("%"+word+"%"))
            # print(conn.fetchall())
    conn.close()

    response = make_response(render_template("bad_search.html", search=search, results=results))
    response.headers['X-XSS-Protection'] = '0'

    return response


def forum():
    return render_template("forum.html")
