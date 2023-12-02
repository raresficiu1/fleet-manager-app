from flask import Flask
from flask_cors import CORS


app = Flask(__name__)

#Members API Route
#jenkins
@app.route("/members")
def members():
    return{"members":['Member1','member2']}


if __name__ == "__main__":
    app.run(debug=True)
    CORS(app)
