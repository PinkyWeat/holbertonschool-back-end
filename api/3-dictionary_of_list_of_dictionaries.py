#!/usr/bin/python3
<<<<<<< HEAD
"""
frite a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
=======
"""frite a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
>>>>>>> 3df843b6449bea8213f1783333273e8c3c04308b
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_request = requests.get(
        'http://jsonplaceholder.typicode.com/users/').json()
    todos_req = requests.get(
        'http://jsonplaceholder.typicode.com/todos').json()
    dic = {}
    for u in user_request:
        uid = u.get('id')
        name = u.get('username')
        dic[uid] = []
        for i in todos_req:
            aux = {}
            if i.get('userId') == int(uid):
                aux['task'] = i.get('title')
                aux['completed'] = i.get('completed')
                aux['username'] = name
                dic[uid].append(aux)

<<<<<<< HEAD
    key = "{}".format(sys.argv[1])
    container = {}
    container[key] = []
    for task in response:
        to_dump = {}
        to_dump['task'] = task.get('title')
        to_dump['username'] = user_response['username']
        to_dump['completed'] = task.get('completed')
        container[key].append(to_dump)
        with open("todo_all_employees.json", 'w+') as f:
            json.dump(container, f)
=======
    with open("todo_all_employees.json", "w", encoding='utf-8') as f:
        json.dump(dic, f)
>>>>>>> 3df843b6449bea8213f1783333273e8c3c04308b
