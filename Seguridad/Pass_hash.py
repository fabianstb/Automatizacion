import sqlite3
import hashlib
from flask import Flask, request

app = Flask(__name__)
db_name = 'test.db'

@app.route('/')
def index():
    return 'Welcome to the hands-on lab for an evolution of password systems!'

@app.route('/signup/v2', methods=['POST'])
def signup_v2():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH
               (USERNAME TEXT PRIMARY KEY NOT NULL,
                HASH TEXT NOT NULL);''')
    conn.commit()
    hash_value = hashlib.sha256(request.form['password'].encode()).hexdigest()
    try:
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH) VALUES (?, ?)",
                  (request.form['username'], hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        return "username has been registered."
    return "signup success"

def verify_hash(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT HASH FROM USER_HASH WHERE USERNAME = ?", (username,))
    records = c.fetchone()
    conn.close()
    return records and records[0] == hashlib.sha256(password.encode()).hexdigest()

@app.route('/login/v2', methods=['POST'])
def login_v2():
    if verify_hash(request.form['username'], request.form['password']):
        return 'login success'
    else:
        return 'Invalid username/password'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
