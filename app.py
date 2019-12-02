from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv
import json
import subprocess
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/email", methods=["POST"])
def sendEmail():
    key = os.getenv("SENDGRID_KEY")
    response = requests.post(
        "https://api.sendgrid.com/v3/mail/send",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        data=json.dumps(request.get_json(force=True))
    )
    print(response)
    return ''


if __name__ == '__main__':
    print(os.getenv("PORT"))
    app.run(debug=True, port=os.getenv("PORT"))
