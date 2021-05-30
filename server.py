from flask import Flask

PORT = 8000
MESSAGE = "Hello world from simplilearn\n"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__master__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
