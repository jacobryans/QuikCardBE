from flask import Flask, jsonify, request
from dotenv import load_dotenv
import json
import subprocess
import os

app = Flask('email')

@app.route("/email", methods=["POST"])
def sendEmail():
    key = os.getenv("SENDGRID_KEY")
    subprocess.call([
    'curl',
    '-X',
    'POST',
    "https://api.sendgrid.com/v3/mail/send",
    "-H",
    f"Authorization: Bearer {key}",
    "-H",
    "Content-Type: application/json",
    '-d',
    json.dumps(request.get_json(force=True))
    ])
    return ''


if __name__ == '__main__':
    print(os.getenv("PORT"))
    app.run(debug=True, port=os.getenv("PORT"))