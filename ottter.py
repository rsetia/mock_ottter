from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/<path:subpath>", methods=['POST', 'GET'])
def ifttt_api(subpath):
    if os.path.isdir(subpath):
        return send_from_directory(subpath, "file")
    else: 
        dirname, basename = os.path.split(subpath)
        return send_from_directory(dirname, basename)
