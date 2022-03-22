from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    diy = 366
else:
    diy = 365
d0 = date(2021, 4, 24)
d1 = date.today()


def days_since():
    return str((d1 - d0).days)


def days_left():
    return str((diy - int(days_since())))


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', d_since=days_since(), d_left=days_left(), d_in_year=diy)


if __name__ == '__main__':
    app.run()
