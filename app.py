from flask import Flask, render_template
from base64 import b64decode

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('template.html', phrase=b64decode(b'0L/QuNGC0L7QvdCw').decode('utf-8'))