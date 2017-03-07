import sqlite3
from settings import DB_NAME

def reset_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS links")
    c.execute('CREATE TABLE links (title text, desc text, link text)')
    # Insert a row of data
    links = [
        ('Facebook', 'Facebook: A social network', 'https://www.facebook.com'),
        ('FMF-Facebook', 'FMF-Facebook: FMF social website', 'https://www.facebook.com/fmf.ul/'),
        ('Google', 'Google: A search engine', 'https://www.google.com'),
        ('FMF', 'FMF: University of Ljubljana. Faculty official page', 'https://www.fmf.uni-lj.si'),
    ]
    c.executemany("INSERT INTO links VALUES (?,?,?)", links)

    c.execute("DROP TABLE IF EXISTS users")
    c.execute('CREATE TABLE users (name text, username text, password text)')
    # Insert a row of data
    users = [
        ('Maks Kolman', 'maks', 'password'),
        ('Administrator Strani', 'admin', 'correcthorsebatterystaple'),
        ('Janez Novak', 'jani', 'banana'),
        ('Marija Sveta', 'marii', 'Tr0ub4dor&3'),
    ]
    c.executemany("INSERT INTO users VALUES (?,?,?)", users)

    c.execute("DROP TABLE IF EXISTS posts")
    c.execute('CREATE TABLE posts (author text, title text, content text)')
    # Insert a row of data
    posts = [
        ('Maks Kolman', 'Happy day', 'I am having such a great day today and just wanted to share it with everyone!'),
        ('Marija Sveta', 'Inconsiderate', 'Did you think how would that make me feel?\nYour literally Hitler for saying this.'),
    ]
    c.executemany("INSERT INTO posts VALUES (?,?,?)", posts)

    # Save (commit) the changes
    conn.commit()
    conn.close()
    return "OK"
