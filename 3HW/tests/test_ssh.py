import re
import requests

from ssh_5.connection.connection import SSH


def ssh_connection(cmd):
    with SSH(hostname='192.168.0.108', username='root', password='password', port=2222) as ssh:
        return ssh.exec_cmd(cmd)


class TestClients:

    def test_ssh(self):
        command = "tail -n 1 /var/log/messages | cut -d ' ' -f 6,7,8,10,11,12"
        assert ssh_connection(command) == 'systemd-logind: New session of user root.\n'

    def test_nginx_ssh(self):
        command = "netstat -tulpn | grep nginx"
        par = re.split(" +", ssh_connection(command))
        assert par[3] == '0.0.0.0:8888' and par[5] == 'LISTEN'

    def test_nginx_http(self):
        hostname = '192.168.0.108'
        port = 8888
        url = f'http://{hostname}:{port}'

        result = requests.get(url)
        assert result.status_code == 200

    def test_nginx_access(self):
        hostname = '192.168.0.108'
        port = 8888
        client = '192.168.0.105'
        url = f'http://{hostname}:{port}'
        result = requests.get(url)
        assert result.status_code == 200

        command = "tail -n 1 /var/log/nginx/access.log | cut -d ' ' -f 6,7,8,9"
        result = ssh_connection(command)
        assert result == '"GET / HTTP/1.1" 200\n'

    def test_firewalld(self):
        hostname = '192.168.0.108'
        port = 8888
        command = f'firewall-cmd --zone=public --remove-port={port}/tcp'
        ssh_connection(command)

        url = f'http://{hostname}:{port}'
        try:
            requests.get(url)
        except:
            command = f'systemctl -l status nginx'
            result = ssh_connection(command).split("\n")
            assert 'Active: active (running)' in result[2]
