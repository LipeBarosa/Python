from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

posts = [
        {
            "title": "Meu primeiro Post",
            "body": "Texto do post",
            "username": "Felipe",
            "created": datetime(2022,7,27)

        },
        {
            "title": "Meu segundo Post",
            "body": "Texto do post",
            "username": "Felipe",
            "created": datetime(2022,7,27)
        }
    ]


@app.route("/")
def hello():
    return render_template("index.html" , posts=posts)



   






