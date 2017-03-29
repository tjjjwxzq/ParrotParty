import os
import string
import random
import re
import sqlite3
from functools import wraps
from flask import Flask, g, render_template, url_for, request, session, abort, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
mail = Mail(app)

# Database setup
DATABASE = 'database.db'


def get_db():
    db = g.get('_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = g.get('_database', None)
    if db is not None:
        db.close()

# CSRF protection


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


def generate_csrf_token(random=False):
    if '_csrf_token' not in session:
        if random:
            session['_csrf_token'] = ''.join(
                random.choice(string.ascii_lowercase) for i in range(10))
        else:
            session['_csrf_token'] = 'avianparty'
        return session['_csrf_token']


app.jinja_env.globals['csrf_token'] = generate_csrf_token


# Check member password

PASSWORD = 'ytraptorrap'


def require_member(f):
    @wraps(f)
    def check_member(*args, **kwargs):
        password = session.get('password')
        if password == PASSWORD:
            return f(*args, **kwargs)
        else:
            password = request.form.get('password')
            if password == PASSWORD:
                session['password'] = password
                return f(*args, **kwargs)
            else:
                return render_template(
                    'index.html', error='That was a pathetic password you pig')
    return check_member

# Views


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/party-parrots', methods=['GET', 'POST'])
@require_member
def member_index():
    return render_template('member_index.html')


@app.route('/send_invite', methods=['POST'])
@require_member
def send_invite():
    email = request.form.get('email')
    if not re.match('\w+@\w+.\w{3}', email):
        return render_template('member_index.html',
                               error='Please input a valid email address')
    else:
        msg = Message(subject='Your Super Exklusive Password',
                      recipients=[email],
                      body=PASSWORD)
        mail.send(msg)
        return render_template('member_index.html')
