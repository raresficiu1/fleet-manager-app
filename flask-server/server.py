from flask import Flask
from flask_cors import CORS


app = Flask(__name__)

#Members API Route
@app.route("/members")
def members():
    return{"members":['MEMBER6969696','member2']}

#jk tst
if __name__ == "__main__":
    app.run(debug=True)
    CORS(app)
