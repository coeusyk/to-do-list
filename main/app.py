from flask import Flask, render_template, redirect, request

from main.models import db


app = Flask(__name__, instance_relative_config=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"  # Setting a basic sqlite server for the database
app.app_context().push()

db.init_app(app)
db.create_all()


@app.route("/")
def redirector():
    return redirect("/today")


@app.route("/today", methods=["GET", "POST"])
def today_window():
    if request.method == "POST":
        pass

    else:
        return render_template("today-window.html")


if __name__ == "__main__":
    app.run(debug=True)
