from django.db import connection
from faker import Faker
from time import time


def select_poc_data():
    with connection.cursor() as cursor:
        query = "select * from test_data;"
        cursor.execute(query)
        rows = cursor.fetchall()
    return rows


def insert_into_db():
    f = Faker()
    t = time()
    with connection.cursor() as cursor:
        for i in range(1499998, 1500000):
            query = f"insert into test_data (order_id, create_date, mobile) values ({i}, '{f.date_time()}', '{f.name()}');"
            cursor.execute(query)
    return time() - t


def select_within_date(s_date="2000-02-01", e_date="2014-03-01"):
    with connection.cursor() as cursor:
        query = f"""
        SELECT * FROM "public".test_data 
        WHERE create_date 
        BETWEEN '{s_date}' AND '{e_date}';
        """
        cursor.execute(query)
        rows = cursor.fetchall()
    return rows
