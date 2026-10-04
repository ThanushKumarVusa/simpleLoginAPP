from flask import Flask, render_template, request
from db import get_connection

app = Flask(__name__)


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT * FROM users
                WHERE username = %s AND password = %s
            """

            cursor.execute(sql, (username, password))
            user = cursor.fetchone()

        if user:
            return render_template(
                "welcome.html",
                username=user["username"]
            )

        return render_template(
            "login.html",
            error="Invalid username or password"
        )

    finally:
        connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
