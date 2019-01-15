import json

from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def hello():
    return Response(response=json.dumps({'hello': 'world'}),
                    status=200,
                    mimetype="application/json")


@app.route('/post', methods=["POST"])
def echo():

    return Response(response=json.dumps(request.json),
                    status=200,
                    mimetype="application/json")


@app.route("/post/<status>", methods=["POST"])
def echo_with_status(status):
    return Response(response=json.dumps(request.json),
                    status=status,
                    mimetype="application/json")


if __name__ == "__main__":
    app.run()
