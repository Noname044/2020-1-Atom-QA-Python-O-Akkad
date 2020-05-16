import os
import re


def total_number(logs):
    return sum(1 for line in logs)


def check_by_type(logs):
    types = {}
    for line in logs:
        a = line.split()
        if a[5] not in types:
            types[a[5]] = 1
        else:
            types[a[5]] += 1
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


if __name__ == "__main__":
    print("Input directory and file name:")
    inp = input()
    if not os.path.exists(inp):
        print("This file is not exist! Bye...")
        exit(99)
    f = open(inp, 'r')
    logs = f.readlines()
    f.close()
    if not os.path.exists('./statistick_py.txt'):
        os.system('touch ./statistick_py.txt')
    f = open('./statistick_py.txt', 'w')
    # check total number of requests
    f.write("Total number of requests: {num}\n\n".format(num=total_number(logs)))
    # check number of requests by type
    type = check_by_type(logs)
    f.write("Number of requests by type:\nType      Number\n")
    for k in type:
        f.write("{key}      {type}\n". format(key=k, type=type[k]))
    # top 10 by size
    top = check_by_size(logs)
    f.write("\nTop 10 by size:\nNumber URL                  CodeSize          Count\n")
    count = 1
    for k in top:
        f.write("{cnt}      {key}      {code}\n".format(cnt=count, key=k, code=top[k]))
        if count == 10:
            break
        count += 1
    # top 10 by number of requests with client error
    top = check_by_client(logs)
    f.write("\nTop 10 by number of requests with client error:\nNumber URL                  CodeIP       "
            "          Count\n")
    count = 1
    for k in sorted(top, key=top.get, reverse=True):
        f.write("{cnt}      {key}      {code}\n".format(cnt=count, key=k, code=top[k]))
        if count == 10:
            break
        count += 1
    # top 10 by number of requests with redirect
    top = check_by_redirect(logs)
    f.write("\nTop 10 by number of requests with redirect:\nNumber URL                  CodeIP       "
            "          Count\n")
    count = 1
    for k in sorted(top, key=top.get, reverse=True):
        f.write("{cnt}      {key}      {code}\n".format(cnt=count, key=k, code=top[k]))
        if count == 10:
            break
        count += 1
    f.close()


class CheckingLogs(object):
    pass
