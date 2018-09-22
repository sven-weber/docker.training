from flask import Flask, Response
import os
import socket
import time

app = Flask(__name__)

# Enable debugging if the DEBUG environment variable is set and starts with Y
app.debug = os.environ.get("DEBUG", "").lower().startswith('y')

hostname = socket.gethostname()

@app.route("/")
def index():
    return ReadFromFile()

#read the current token message from the file 
def ReadFromFile():
    try:
        f = open('serverfiles/token.txt','r')
        message = f.read() 
        f.close() 
    except:
        message = "No command defined yet!"
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=False)