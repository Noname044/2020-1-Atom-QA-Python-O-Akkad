from mock_4.mock.mock import users


def add_user(user_id: int, user_data: dict):
    users.update({str(user_id): user_data})


def test_get(mock_server, socket_client):
    server_host, server_port = mock_server
    client = socket_client

    user = {'name': 'Oleg', 'surname': 'Akkad'}
    id_u = 123

    url = f'http://{server_host}:{server_port}/user/{id_u}'
    result = client.get_request(id_u)
    res = result[-1].split("\"")
    assert res[3] == user['name'] and res[7] == user['surname']


def test_post(mock_server, socket_client):
    server_host, server_port = mock_server
    client = socket_client

    user = {'7': {'name': 'Jacky', 'surname': 'Chan'}}
    id_u = 7

    url = f"http://{server_host}:{server_port}/user/{id_u}"
    result = client.get_request(id_u)
    res = result[0].split(" ")
    assert res[1] == '404'

    url = f'http://{server_host}:{server_port}/{user}/{str(id_u)}'
    name = client.post_request(user, id_u)
    res = name[0].split(" ")
    assert res[1] == '200'

    result = client.get_request(id_u)
    res = result[0].split(" ")
    assert res[1] == '200'
