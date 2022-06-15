from django.shortcuts import render


def SignUpView(request):
    return render(request, "users/simple_view.html", {})
