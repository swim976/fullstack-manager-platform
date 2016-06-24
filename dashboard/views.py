from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')


def peoples(request):
    return render(request, 'people_list.html')
