from flask import Flask, redirect, request, url_for

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


if __name__ == '__main__':
    app.run()
