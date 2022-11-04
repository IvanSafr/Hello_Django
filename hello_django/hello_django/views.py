from django.http import HttpResponse
from django.shortcuts import render

# Функции отображения на запрос на сайте
def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, "home.html")
