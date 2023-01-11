import os
from flask import Flask
import datetime


from datetime import date

app = Flask(__name__)

@app.route('/')
def hello():

    e = datetime.datetime.now()
    name = os.environ.get('NAME')
    return f"{e.day}/{e.month}/{e.year} {e.hour}:{e.minute}  Hello {name}!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

