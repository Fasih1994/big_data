from django.urls import path, include

from api.views import hello_world, test_query, insert_into_database, select_within

urlpatterns = [
    path('hello/', hello_world),
    path('test_query/', test_query),
    path('insert_data/', insert_into_database),
    path('select_within/', select_within)
]
