from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from api.queries import select_poc_data, insert_into_db, select_within_date
from time import time


# Create your views here.
def hello_world(request):
    response_data = {
        'id': 4,
        'name': 'Test Response',
        'roles': ['Admin', 'User']
    }
    return JsonResponse(response_data)


def test_query(request):
    t = time()
    data = select_poc_data()
    data_in_json = {element[0]: element[1:] for element in data}
    # print(data_in_json)
    print(f"took {time()-t}seconds to select")
    return JsonResponse(data_in_json)


def insert_into_database(request):
    print("received")
    time = insert_into_db()
    return JsonResponse({"message": f"Query executed successfully in  {time}."})


def select_within(request):
    t = time()
    try:
        s_date = request.GET['s_date']
        e_date = request.GET['e_date']
        data = select_within_date(s_date, e_date)
    except KeyError:
        data = select_within_date()
    except Exception as e:
        raise
    finally:
        data_in_json = {element[0]: element[1:] for element in data}
        print(f"took {time() - t }seconds to select")
        return JsonResponse(data_in_json)
