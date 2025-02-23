from flask import (Flask, render_template,
                   request, jsonify, abort)
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from db import db
from model import Users


load_dotenv()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

db.init_app(app)

@app.route('/')
def hello():
    return render_template("layout.html")

@app.route('/user_tracking/', methods=['POST'])
def user_tracking():
    user_data = request.json               # gets the user data sent from the browser in the HTTP request payload
    response_data = {"status": "success"}  # displaying success if data received successfully

    if not user_data:
        abort(404)

    return jsonify(response_data), 200

@app.route('/user_login', methods=['POST'])
def user_login():
    username = request.json.get("username", None)
    user = db.one_or_404(db.select(Users).filter_by(username=username))
    response_data = {"status": "success", "username": user.username}
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)

