#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    Export data in the CSV format.
"""
import csv
import requests
import sys


def Create_CSV_file_tasks(ID):
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

    # Creates and open CSV file.
    csv_filename = f'{ID}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    # Loops to get infos to be writes in the CSV file.
        for task in tasks:
            task_completed = 'True' if task.get('completed') else 'False'
            format_row = [ID, user_name, task_completed, task.get('title')]

            # Writes row in the CSV file.
            writer.writerow(format_row)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    id = int(sys.argv[1])
    Create_CSV_file_tasks(id)
