import os
import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)

    return cursor.fetchone()


def run_command(user_input):
    os.system(user_input)


def calculate(expression):
    return eval(expression)