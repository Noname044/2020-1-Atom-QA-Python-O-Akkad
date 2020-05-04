import os
import re

from mysql_3.mysql_client.mysql_client import MysqlConnector


def total_number(logs):
    return sum(1 for line in logs)


def check_by_type(logs):
    types = {}
    for line in logs:
        a = line.split()
        str = a[5].replace("\"", "")
        if str not in types:
            types[str] = 1
        else:
            types[str] += 1
    return types


def check_by_size(logs):
    top_1 = {}
    lst = [x.rstrip('\n').split()[0:] for x in logs]
    lst = sorted(lst, key=lambda x: int(x[9]), reverse=True)
    for a in lst:
        a = a[6] + ' ' + a[8] + ' ' + a[9]
        if a not in top_1:
            top_1[a] = 1
        else:
            top_1[a] += 1
    return top_1


def check_by_client(logs):
    top_2 = {}
    for line in logs:
        a = line.split()
        if not re.match(r'4\d\d', a[8]):
            continue
        a = a[6] + ' ' + a[8] + ' ' + a[0]
        if a not in top_2:
            top_2[a] = 1
        else:
            top_2[a] += 1
    return top_2


def check_by_redirect(logs):
    top_3 = {}
    for line in logs:
        a = line.split()
        if not re.match(r'3\d\d', a[8]):
            continue
        a = a[6] + ' ' + a[8] + ' ' + a[0]
        if a not in top_3:
            top_3[a] = 1
        else:
            top_3[a] += 1
    return top_3


class CheckingLogs:

    def __init__(self, connection: MysqlConnector):
        self.connection = connection

    def main(self, inp):
        if not os.path.exists(inp):
            print("This file is not exist! Bye...")
            exit(99)
        f = open(inp, 'r')
        logs = f.readlines()
        f.close()

        # check total number of requests
        num = total_number(logs)
        self.connection.execute_query(f'insert into total_number (total)  values ({num})')

        # check number of requests by type
        type = check_by_type(logs)
        for k in type:
            self.connection.execute_query(f"INSERT number_of_requests(Type, Number)  VALUES ('{k}', '{type[k]}');")

        # top 10 by size
        top = check_by_size(logs)
        count = 1
        for k in top:
            str = k.split()
            self.connection.execute_query(f"insert into top10_by_size (Number, URL, Code, Size, Count)"
                                          f"  values ('{count}','{str[0]}','{str[1]}','{str[2]}','{top[k]}')")
            if count == 10:
                break
            count += 1

        # top 10 by number of requests with client error
        top = check_by_client(logs)
        count = 1
        for k in sorted(top, key=top.get, reverse=True):
            str = k.split()
            self.connection.execute_query(f"insert into top10_by_client_error (Number, URL, Code, IP, Count)"
                                          f"  values ('{count}','{str[0]}','{str[1]}','{str[2]}','{top[k]}')")
            if count == 10:
                break
            count += 1

        # top 10 by number of requests with redirect
        top = check_by_redirect(logs)
        count = 1
        for k in sorted(top, key=top.get, reverse=True):
            str = k.split()
            self.connection.execute_query(f"insert into top10_by_redirect (Number, URL, Code, IP, Count)"
                                          f"  values ('{count}','{str[0]}','{str[1]}','{str[2]}','{top[k]}')")
            if count == 10:
                break
            count += 1
