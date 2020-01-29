import json
import time
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/hello')
def hello():
    return Response(response=json.dumps({'hello': 'world'}),
                    status=200,
                    mimetype="application/json")

#
# @app.route('/post', methods=["POST"])
# def echo():
#     print(request.json)
#     return Response(response=json.dumps(request.json),
#                     status=200,
#                     mimetype="application/json")
#
#
# @app.route("/post/<status>", methods=["POST"])
# def echo_with_status(status):
#     if status == '0':
#         time.sleep(10)
#     return Response(response=json.dumps(request.json),
#                     status=status,
#                     mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
