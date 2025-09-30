import sqlite3

def get_user_by_username(username: str) -> dict:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, email TEXT)")
    cursor.execute("INSERT INTO users (username, email) VALUES ('bob', 'bob@example.com')")
    query = "SELECT id, username, email FROM users WHERE username = '%s'" % username
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "username": row[1], "email": row[2]}
    return {}
