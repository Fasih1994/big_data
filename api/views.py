from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from api.queries import select_poc_data


# Create your views here.
def hello_world(request):
    response_data = {
        'id': 4,
        'name': 'Test Response',
        'roles': ['Admin', 'User']
    }
    return JsonResponse(response_data)


def test_query(request):
    data = select_poc_data()
    data_in_json = {element[0]: element[1:] for element in data}
    print(data_in_json)
    return JsonResponse(data_in_json)
