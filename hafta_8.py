#flask
from flask import Flask
app = Flask(__name__)
@app.route("/")
def merhaba():
    return "<p>merhaba</p>"
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=22222)