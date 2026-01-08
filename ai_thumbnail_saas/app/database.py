import sqlite3

conn = sqlite3.connect("data/users.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
  user_id INTEGER PRIMARY KEY,
  credits INTEGER DEFAULT 0
)
""")

conn.commit()

def get_user(uid):
    cur.execute("SELECT credits FROM users WHERE user_id=?", (uid,))
    r = cur.fetchone()
    if not r:
        cur.execute("INSERT INTO users VALUES (?,0)", (uid,))
        conn.commit()
        return 0
    return r[0]

def add_credits(uid, n):
    cur.execute("UPDATE users SET credits=credits+? WHERE user_id=?", (n, uid))
    conn.commit()

def deduct_credit(uid):
    cur.execute("UPDATE users SET credits=credits-1 WHERE user_id=?", (uid,))
    conn.commit()
