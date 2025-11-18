from django.http import HttpResponse
from django.shortcuts import render

#function based
#
# def home(request):
#     return HttpResponse("Welcome to  life")
# def index(request):
#     return HttpResponse('index page')
# def new(request):
#     return HttpResponse("life is hard")


def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')

