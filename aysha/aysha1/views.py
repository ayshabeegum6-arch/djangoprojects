from django.http import HttpResponse

from django.shortcuts import render





def home(request):
    context={'name':'Aysha','age':'22'}
    return render(request,'home.html',context)

def viewbooks(request):
    return render(request,'viewbooks.html')

def addbooks(request):
    return render(request,'addbooks.html')

def index(request):
    return render(request,'index.html')
