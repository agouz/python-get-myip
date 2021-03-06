from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    response = {
        'headers': request.headers,
        'ip': request.remote_addr
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run()