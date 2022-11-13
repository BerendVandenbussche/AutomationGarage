from database import database
from dotenv import load_dotenv
from flask import Flask, jsonify, request, url_for, json
from flask_cors import CORS
import os

load_dotenv()
app = Flask(__name__)
CORS(app)
conn = database(app=app, user=os.getenv('DATABASEUSER'), password=os.getenv('DATABASEPASSWORD'), db=os.getenv('DATABASENAME'))


if __name__ == '__main__':
    Flask.run(app, host="0.0.0.0", port=5000)