from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("secure_users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("DELETE FROM users")
    c.execute("INSERT INTO users VALUES ('admin', 'password123')")
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("secure_users.db")
        c = conn.cursor()
        # ✅ Parameterized Query (safe)
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = c.fetchone()
        if result:
            message = "Login successful!"
        else:
            message = "Login failed."
        conn.close()
    return render_template_string("""
        <h2>Login (Secure)</h2>
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
        <p>{{message}}</p>
    """, message=message)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
