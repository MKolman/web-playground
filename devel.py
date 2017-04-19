import sqlite3
from settings import DB_NAME
from flask import session, render_template, request


def reset_db():
    if request.method == "POST" and request.form.get("pass") == "cjfytr8732DCsjhg87fajbhbf87wefbjh":
        session.clear()
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS links")
        c.execute('CREATE TABLE links (title text, desc text, link text, hide integer)')
        # Insert a row of data
        links = [
            ('Facebook', 'Facebook: A social network', 'https://www.facebook.com', '0'),
            ('FMF-Facebook', 'FMF-Facebook: FMF social website', 'https://www.facebook.com/fmf.ul/', '0'),
            ('Google', 'Google: A search engine', 'https://www.google.com', '0'),
            ('FMF', 'FMF: University of Ljubljana. Faculty official page', 'https://www.fmf.uni-lj.si', '0'),

            ('Secret Facebook', ' Secret Facebook: A social network', 'https://www.facebook.com', '1'),
            ('Secret FMF-Facebook', 'Secret FMF-Facebook: FMF social website', 'https://www.facebook.com/fmf.ul/', '1'),
            ('Secret Google', 'Secret Google: A search engine', 'https://www.google.com', '1'),
            ('Secret FMF', 'Secret FMF: University of Ljubljana. Faculty official page', 'https://www.fmf.uni-lj.si', '1'),
            ('Secret Database', 'Database viewer', '/db_viewer_XDSie983BQbnxc_asjdh', '1'),
        ]
        c.executemany("INSERT INTO links VALUES (?,?,?,?)", links)

        c.execute("DROP TABLE IF EXISTS users")
        c.execute('CREATE TABLE users (name text, username text PRIMARY KEY, password text, funds integer)')
        # Insert a row of data
        users = [
            ('Maks Kolman', 'maks', 'password', 100),
            ('Administrator Strani', 'admin', 'correcthorsebatterystaple', 100),
            ('Janez Novak', 'jani', 'banana', 100),
            ('Marija Novak', 'marii', 'Tr0ub4dor&3', 100),
        ]
        c.executemany("INSERT INTO users VALUES (?,?,?,?)", users)
        c.execute("PRAGMA foreign_keys = ON;")

        c.execute("DROP TABLE IF EXISTS posts")
        c.execute('CREATE TABLE posts (author text REFERENCES users(username), title text, content text, img text)')
        # Insert a row of data
        posts = [
            ('maks', 'Happy day', 'I am having such a great day today and just wanted to share it with everyone!', 'http://icons.iconarchive.com/icons/jonathan-rey/simpsons/256/Homer-Simpson-04-Happy-icon.png'),
            ('marii', 'Inconsiderate', 'Did you think how would that make me feel?<br/>Your literally Hitler for saying this.', ''),
            ('jani', 'Much fun!', 'Hello fellow humans.<br/> I made billions of dollars just watching cute bunnies and you can too. Just go to <a href="evil_bun">this link.</a>', 'https://at-cdn-s01.audiotool.com/2013/02/26/documents/csCEKYagXloFZUwjZ9Y7aUlZ6PGP/0/cover256x256-df6ac55d007f48aaa31b00bdf487e9e2.jpg'),
        ]
        c.executemany("INSERT INTO posts VALUES (?,?,?,?)", posts)


        c.execute("DROP TABLE IF EXISTS stolen")
        c.execute('CREATE TABLE stolen (data text)')

        # Save (commit) the changes
        conn.commit()
        conn.close()
        return render_template("reset_db.html", success=True)
    return render_template("reset_db.html")


if __name__ == "__main__":
    reset_db()
