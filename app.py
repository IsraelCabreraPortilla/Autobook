from flask import Flask, render_template, request
import pandas as pd

from urllib.request import urlopen

app = Flask(__name__)


@app.route('/', methods=["get", "post"])

def submit():
    blotter = request.form.get("blotter")
    hedgeid = request.form.get("hedgeid")
    tabname = request.form.get("tabname")
    credspath = request.form.get("credspath")
    print(blotter,hedgeid,tabname,credspath)


    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)