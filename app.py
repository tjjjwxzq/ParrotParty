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


def create_plea_tables():
    db= get_db()
    cur = db.cursor()
    cur.execute('''create table if not exists plea_table(content_plea text)''')
    db.commit()
    db.close()
# CSRF protection


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


def generate_csrf_token(random_token=False):
    if '_csrf_token' not in session:
        if random_token:
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

#create the plea tables
@app.route('/')
def index():
    create_plea_tables()
    return render_template('index.html')



@app.route('/party-parrots', methods=['GET', 'POST'])
@require_member
def member_index():
    db= get_db()
    cur = db.cursor()
    pleas=[]
    for c in cur.execute('SELECT * FROM plea_table'):
        pleas.append(c[0])
    db.commit()
    db.close()

    return render_template('member_index.html',plea_list=pleas)


#write the pleas into the database
@app.route('/request-invite',methods=['POST'])
def plea_index():
    plea_input = request.form.get('_plea')
    db= get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO plea_table VALUES (?)",(plea_input,))
    db.commit()
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
@require_member
def calculate():
    calc_input = request.form.get('_calculator')
    if calc_input:
        if re.match('([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)', calc_input):
            return render_template('member_index.html', solution=eval(calc_input))
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
