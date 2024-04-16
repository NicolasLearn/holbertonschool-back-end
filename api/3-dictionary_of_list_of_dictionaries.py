#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    Export data in the JSON format.
"""
import json
import requests
import sys


def Create_JSON_file_tasks_all():
    """ Used the module requests to get infos on the users, with API.

    Args:
        ID(int): ID to the employee to be searched.
    """

    # Sets Urls variables to share info with the API.
    api_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users".format(api_url)

    # HTTP Request to get all users.
    users = requests.get(users_url).json()

    all_tasks = {}
    # Loops to get all info for each user.
    for user in users:
        id = user.get('id')
        username = user.get('username')

        # HTTP Request to get all tasks for the user.
        tasks = requests.get("{}/{}/todos".format(users_url, id)).json()

        tasks_list = []
        for task in tasks:
            title = task.get('title')
            status = task.get('completed')
            dict = {
                "username": username,
                "task": title,
                "completed": status
            }
            tasks_list.append(dict)
            all_tasks[str(id)] = tasks_list

    # Creates, open and writes into the JSON file.
    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == '__main__':
    Create_JSON_file_tasks_all()
