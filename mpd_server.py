from flask import Flask, send_from_directory, Response
import os

app = Flask(__name__)

DASH_DIR = os.path.join(os.getcwd(), "dash")


# Serve MPD manifest
@app.route("/mpd_stream")
def mpd():
    response = send_from_directory(DASH_DIR, "globo.mpd")
    response.headers["Content-Type"] = "application/dash+xml"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


# Serve all DASH segment files
@app.route("/<path:filename>")
def dash_files(filename):
    response = send_from_directory(DASH_DIR, filename)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)