from django.urls import path

from users.views import SignUpView

urlpatterns = [
    path('', SignUpView, name='signup'),
]
