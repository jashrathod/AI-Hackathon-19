from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
# import digit
import bcrypt
import base64
import warnings
import json
from bson import json_util

warnings.filterwarnings("ignore")

app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'db'
# app.config['MONGO_URI'] = 'mongodb://0.0.0.0:27017/db'

# mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    print(projectpath)
    return projectpath


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.debug = True
    app.run(host='0.0.0.0', port="1000")