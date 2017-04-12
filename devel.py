import sqlite3
from settings import DB_NAME

def reset_db():
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
    ]
    c.executemany("INSERT INTO links VALUES (?,?,?,?)", links)

    c.execute("DROP TABLE IF EXISTS users")
    c.execute('CREATE TABLE users (name text, username text PRIMARY KEY, password text)')
    # Insert a row of data
    users = [
        ('Maks Kolman', 'maks', 'password'),
        ('Administrator Strani', 'admin', 'correcthorsebatterystaple'),
        ('Janez Novak', 'jani', 'banana'),
        ('Marija Novak', 'marii', 'Tr0ub4dor&3'),
    ]
    c.executemany("INSERT INTO users VALUES (?,?,?)", users)
    c.execute("PRAGMA foreign_keys = ON;")

    c.execute("DROP TABLE IF EXISTS posts")
    c.execute('CREATE TABLE posts (author text REFERENCES users(username), title text, content text)')
    # Insert a row of data
    posts = [
        ('maks', 'Happy day', 'I am having such a great day today and just wanted to share it with everyone!'),
        ('marii', 'Inconsiderate', 'Did you think how would that make me feel?\nYour literally Hitler for saying this.'),
    ]
    c.executemany("INSERT INTO posts VALUES (?,?,?)", posts)


    c.execute("DROP TABLE IF EXISTS stolen")
    c.execute('CREATE TABLE stolen (data text)')

    # Save (commit) the changes
    conn.commit()
    conn.close()
    return "OK"


if __name__ == "__main__":
    reset_db()
