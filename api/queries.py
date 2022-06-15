from django.db import connection


def select_poc_data():
    with connection.cursor() as cursor:
        query = "select * from test_data limit 5;"
        cursor.execute(query)
        rows = cursor.fetchall()
    return rows
