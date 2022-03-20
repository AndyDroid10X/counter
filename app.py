from flask import Flask, render_template
import counter
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

sched = BackgroundScheduler(daemon=True)
sched.add_job(counter, 'interval', minutes=720)
sched.start()


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', count=counter.days_since)


if __name__ == '__main__':
    app.run()
