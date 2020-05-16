import threading

from flask import Flask, abort, request

app = Flask(__name__)
users = {'123': {'name': 'Oleg', 'surname': 'Akkad'},
         '321': {'name': 'Evgeniy', 'surname': 'Gorin'}}
host = '127.0.0.1'
port = 5000


def run_mock():
    server = threading.Thread(target=app.run, kwargs={'host': host, 'port': port})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/user/<user_id>')
def get_request(user_id: int):
    user = users.get(str(user_id), None)
    if user:
        return user
    else:
        abort(404)


@app.route('/user', methods=["POST"])
def post_request():
    id_u = request.form['id']
    name = request.form['name']
    surname = request.form['surname']
    user = {str(id_u): {'name': name, 'surname': surname}}

    users.update(user)
    print(users)
    if name:
        return users
    else:
        abort(404)


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


if __name__ == '__main__':
    run_mock()
