from django.http import HttpResponse
from django.shortcuts import render


def homepage(req):
    return render(req, "home.html")


#     return HttpResponse("Hello World")


def about(req):
    return render(req, "about.html")


#     return HttpResponse("I am Abheesh")
