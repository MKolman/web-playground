import sqlite3

from flask import render_template, request, make_response, session, redirect, g

from settings import DB_NAME


def search():
    search = request.args.get("search")
    results = []

    conn = sqlite3.connect(DB_NAME)
    if search:
        for word in search.split(" ", 1):
            results += conn.execute("SELECT * FROM links WHERE hide=0 and lower(desc) LIKE '%%%s%%'" % word)
            # print(conn.fetchall())
    conn.close()

    response = make_response(render_template("search.html", search=search, results=results))
    response.headers['X-XSS-Protection'] = '0'

    return response


def forum():
    conn = sqlite3.connect(DB_NAME)
    if "user" in session and request.args.get("action") == "new":
        d = request.args
        user = session.get("user")[1]
        title = d.get("title")
        content = d.get("content")
        if user and title and content:
            conn.execute("INSERT INTO posts VALUES (?,?,?)", (user, title, content))

    posts = list(conn.execute("SELECT users.name, posts.title, posts.content FROM posts JOIN users ON posts.author=users.username"))
    conn.commit()
    conn.close()
    print(posts)
    response = make_response(render_template("forum.html", posts=posts))
    response.headers['X-XSS-Protection'] = '0'
    return response


def login():
    if request.args.get("action") == "login":
        name = request.args.get("full_name")
        username = request.args.get("username")
        password = request.args.get("password")

        conn = sqlite3.connect(DB_NAME)
        user = list(conn.execute("SELECT * FROM users WHERE username=?", (username,)))
        if user:
            if user[0][-1] == password:
                session["user"] = user[0]
                g.message = "Logged in!"
            else:
                g.message = "Wrong password!"
        else:
            print((name, username, password))
            conn.executescript("INSERT INTO users VALUES ('%s','%s','%s')" % (name, username, password))
            conn.commit()
            g.message = "New user created"
            session["user"] = (name, username, password)

        print(user)
        conn.close()
    # if success:
    #     return redirect("/forum")
    # else:
    return render_template("login.html")


def evil():
    conn = sqlite3.connect(DB_NAME)
    if request.args.get("save"):
        conn.execute("INSERT INTO stolen VALUES (?)", (str(list(request.args.items())),))
        conn.commit()
    # data = list(conn.execute("SELECT * FROM stolen"))
    conn.close()
    return render_template("evil.html")


def evil_bun():
    return render_template("evil_bun.html")


def db_view():
    table = request.args.get("table", "posts")
    conn = sqlite3.connect(DB_NAME)
    data = list(conn.execute("SELECT * FROM %s" % table))
    header = list(conn.execute("PRAGMA table_info(%s)" % table))
    header = [h[1] for h in header]
    conn.close()
    return render_template("db_view.html", data=data, header=header)
