from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


def index(request):
    lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return render(request, 'article/index.html', {'lst': lst})


