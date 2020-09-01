import os
import sqlite3
from flask import Flask

app = Flask(__name__)
app.config.from_object('api.config.DevConfig')

def get_db_connection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "database.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
