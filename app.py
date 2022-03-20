from flask import Flask, render_template
import counter
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', count=counter.days_since)


if __name__ == '__main__':
    app.run()
