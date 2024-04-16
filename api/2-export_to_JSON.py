#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    Export data in the JSON format.
"""
import json
import requests
import sys


def Create_JSON_file_tasks(ID):
    """ Used the module requests to get infos on the users, with API.

    Args:
        ID(int): ID to the employee to be searched.
    """

    # Sets Urls variables to share info with the API.
    api_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(api_url, ID)
    user_tasks_url = "{}/todos".format(user_url)

    # HTTP Request to get the Name of the employee.
    user = requests.get(user_url).json()
    user_name = user.get("username")

    # HTTP Request to get all tasks of the employee.
    tasks = requests.get(user_tasks_url).json()

    # Loops to be creates JSON data format.
    tasks_list = []
    for task in tasks:
        title = task.get('title')
        status = task.get('completed')
        # Creates dict for each task.
        dict = {"task": title, "completed": status, "username": user_name}
        tasks_list.append(dict)

    # Creates new dict, where key=ID, value=list_of_tasks
    json_data = {str(ID): tasks_list}

    # Creates, open and writes into the JSON file.
    json_filename = f'{ID}.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    id = int(sys.argv[1])
    Create_JSON_file_tasks(id)
