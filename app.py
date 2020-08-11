from flask import Flask, render_template
from base64 import b64decode

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('template.html', phrase=b64decode(b'0YHQv9Cw0YHQuNCx0L4=').decode('utf-8'))