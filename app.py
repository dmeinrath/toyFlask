from flask import Flask, make_response, request, url_for
from flask import stream_with_context
import pandas as pd
import re
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/test', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        request_data = request.data
        return f'here is your data: {request_data}'
    else:
        return 'get works!'


@app.route("/upload", methods=["POST"])
def upload():
    range_header = request.headers.get('Range')
    match = re.search('(?P<start>\d+)-(?P<end>\d+)/(?P<total_bytes>\d+)', range_header)
    start = int(match.group('start'))
    with open("./tmp/output_file.pkl", 'rb+' if os.path.exists("./tmp/output_file.pkl") else 'wb+') as f:
        chunk_size = 4096
        f.seek(start)
        chunk = request.stream.read(chunk_size)
        if len(chunk) == 0:
            return
        f.write(chunk)
    return make_response({"status": "ok"}, 200)


@app.route("/read", methods=["GET"])
def print_pickle():
    print(pd.read_pickle('./tmp/output_file.pkl'))
    return make_response({"status": "ok"}, 200)


if __name__ == '__main__':
    app.run()
