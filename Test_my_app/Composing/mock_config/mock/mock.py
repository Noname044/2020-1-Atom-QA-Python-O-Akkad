import random
import threading

from flask import Flask, request, json

app = Flask(__name__)
users_ids = {123: 'Oleg666',
             321: 'Euguene789'}
host = 'vk_mock'
port = 5000


def run_mock():
    server = threading.Thread(target=app.run, kwargs={'host': host, 'port': port})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/vk_id/<username>')
def get_request(username):
    for k in users_ids:
        if users_ids[k] == username:
            data = {'vk_id': k}
            response = app.response_class(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
            )
            return response
    response = app.response_class(
        response='{}',
        status=404,
        mimetype='application/json'
    )
    return response


@app.route('/<username>/deluser')
def get_request_del(username):
    for k in users_ids:
        if users_ids[k] == username:
            del users_ids[k]
            response = app.response_class(
                response='{}',
                status=404,
                mimetype='application/json'
            )
            return response


@app.route('/<username>/adduser')
def get_request_add(username):
    for k in users_ids:
        if users_ids[k] == username:
            data = {'vk_id': k}
            response = app.response_class(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
            )
            return response
    f = 1
    new_id = random.randint(0, 1000)
    while f:
        new_id = random.randint(0, 1000)
        if new_id not in users_ids.keys():
            f = 0

    new_user = {new_id: username}
    users_ids.update(new_user)
    data = {'vk_id': new_id}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


if __name__ == '__main__':
    run_mock()
