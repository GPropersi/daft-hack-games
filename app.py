from flask import (Flask, render_template,
                   request, jsonify, abort)

app = Flask(__name__)

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

@app.route('/user_login/', methods=['POST'])
def user_login():
    #TODO: If user not in database
    """
    if user not in database: abort(404)
    """

    response_data = {"status": "success"}
    return jsonify(response_data), 200



if __name__ == '__main__':
    app.run(debug=True)

