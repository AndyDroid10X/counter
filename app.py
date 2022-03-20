from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


def counter():
    d0 = date(2021, 4, 24)
    d1 = date.today()
    return str((d1 - d0).days)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', count=counter())


if __name__ == '__main__':
    app.run()
