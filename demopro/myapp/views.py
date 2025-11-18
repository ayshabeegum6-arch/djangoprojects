from django.http import HttpResponse
from django.shortcuts import render

def first(request):
    return HttpResponse("life is hard")
def second(request):
    return HttpResponse("lets fight")
