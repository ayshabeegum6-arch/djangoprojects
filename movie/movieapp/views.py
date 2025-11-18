from django.shortcuts import render,redirect
from movieapp.models import Movie
from django.views import View
from movieapp.forms import MovieForm





class Home(View):

    def get(self, request):
        m=Movie.objects.all()
        context={'movie':m}
        return render(request, 'home.html')




class Addmovies(View):
    def get(self, request):
        form_instance=MovieForm()
        context={'form':form_instance}
        return render(request, 'addmovies.html',context)

    def post(self,request):
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
           form_instance.save()
           context={'form':form_instance}
           return render(request, 'addmovies.html')


class DetailView(View):
    def get(self, request,i):
        m=Movie.objects.get(id=i)
        context={'movie':m}
        return render(request, 'detail.html',context)



class DeleteView(View):
    def get(self, request,i):
        m=Movie.objects.get(id=i)
        m.delete()
        return redirect('home')




