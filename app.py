import os
import sqlite3
from flask import Flask, g, render_template, url_for

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

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


# Views
@app.route('/')
def index():
    return render_template('index.html')
