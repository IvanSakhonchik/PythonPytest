import json
import os

from tests.models.User import User


def convert_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_test_users(file_path):
    test_users_data = convert_json(file_path)
    users = []
    for data in test_users_data:
        user = User(
            data["User№"],
            data["FirstName"],
            data["SecondName"],
            data["Mail"],
            data["Age"],
            data["Salary"],
            data["Department"]
        )
        users.append(user)
    return users


config_data = convert_json(os.path.dirname(os.path.abspath(__file__)) + "\\..\\resources\\config.json")
test_data = convert_json(os.path.dirname(os.path.abspath(__file__)) + "\\..\\..\\tests\\resources\\test_data.json")
test_users = get_test_users(os.path.dirname(os.path.abspath(__file__)) + "\\..\\..\\tests\\resources\\test_users.json")
