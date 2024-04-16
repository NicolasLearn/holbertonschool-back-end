#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    Print information about this last one.
"""
import requests
import sys


def get_users(ID):
    """ Used the module requests to get infos on the users, with API.

    Args:
        ID(int): ID to the employee to be seached.
    """

    # Sets Urls to share info with the API.
    api_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(api_url, ID)
    user_tasks_url = "{}/todos".format(user_url, ID)

    # HTTP Request to get the Name of the employee.
    user = requests.get(user_url).json()
    user_name = user.get("name")

    # HTTP Request to get all tasks of the employee.
    tasks = requests.get(user_tasks_url).json()

    # Get infos on the tasks done or not, of the employee.
    all_tasks = len(tasks)
    done_tasks = sum(task.get("completed", False) for task in tasks)

    # Print the summary of the done tasks.
    print("Employee {} is done with tasks({}/{}):".format(user_name,
          done_tasks, all_tasks))

    # Print the title to the done tasks.
    for done_task in tasks:
        if done_task.get("completed", False):
            print("\t {}".format(done_task.get("title")))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    id = int(sys.argv[1])
    get_users(id)
