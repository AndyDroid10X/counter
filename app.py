from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    dpy = 366
else:
    dpy = 365
d0 = date(2021, 4, 24)
d1 = date.today()


def days_since():
    return (d1 - d0).days


def days_left():
    return dpy - days_since()


@app.route("/since")
def since():
    return render_template('index.html', main_text=str(days_since()))


@app.route("/left")
def left():
    return render_template('index.html', main_text=str(days_left()))


@app.route("/diy")
def diy():
    return render_template('index.html', main_text=str(dpy))


@app.route("/")
def index():  # put application's code here
    return render_template('index.html', main_text="Press the button")


if __name__ == '__main__':
    app.run()
