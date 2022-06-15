from django.urls import path, include

from api.views import hello_world, test_query

urlpatterns = [
    path('hello/', hello_world),
    path('test_query/', test_query)
]
