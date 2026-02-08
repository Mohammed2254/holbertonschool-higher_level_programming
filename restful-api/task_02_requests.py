"""2- restfulapi"""

import json
import requests
import csv


def fetch_and_print_posts():
    data = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {data.status_code}")
    if data.status_code == 200:
        data = data.json()
        for item in data:
            print(f"{item['title']}")


def fetch_and_save_posts():
    data = requests.get("https://jsonplaceholder.typicode.com/posts")
    if data.status_code == 200:
        data = data.json()
        listOfData = []
        for itm in data:
            listOfData.append(
                {"id": itm["id"], "title": itm["title"], "body": itm["body"]}
            )
        with open("posts.csv", "w") as file:
            colums = ["id", "title", "body"]
            CSVf = csv.DictWriter(file, fieldnames=colums)
            CSVf.writeheader()
            CSVf.writerows(listOfData)
