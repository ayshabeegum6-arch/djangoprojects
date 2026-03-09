from django.shortcuts import render,redirect
from movieapp.models import Movie
from movieapp.forms import MovieForm
from django.views import View
# Create your views here.

# def home(request):
#     return render(request,"home.html")
# def addmovie(request):
#     return render(request,"addmovie.html")
class Home(View):
    def get(self,request):
        m = Movie.objects.all()
        context = {'movie': m}
        return render(request,'home.html',context)

class Addmovie(View):
    def get(self,request):

        form_instance=MovieForm()
        context={'form':form_instance}
        return render(request,'addmovie.html',context)
    def post(self,request):
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            context={'form':form_instance}
            return redirect('home')

class DetailView(View):
    def get(self,request,i):
        m=Movie.objects.get(id=i)
        context={'movie':m}

        return render(request,'detail.html',context)

class DeleteView(View):
        def get(self, request, i):
            m=Movie.objects.get(id=i)
            m.delete()
            return redirect('home')

class UpdateView(View):
    def get(self,request,i):
        m = Movie.objects.get(id=i)
        form_instance=MovieForm(instance=m)
        context={'form':form_instance}
        return render(request,'addmovie.html',context)
    def post(self,request,i):
        m = Movie.objects.get(id=i)
        form_instance=MovieForm(request.POST,request.FILES,instance=m)
        if form_instance.is_valid():
            form_instance.save()
            context={'form':form_instance}
            return redirect('home')