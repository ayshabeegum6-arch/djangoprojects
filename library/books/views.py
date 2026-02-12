from django.shortcuts import render,redirect
from django.template.context_processors import request
from django.views import View
from books.forms import Addbookforms
from books.models import Book
# Create your views here.

# def home(request):
#     return render(request,'home.html')
# def viewbooks(request):
#     return render(request,'viewbooks.html')
# def addbooks(request):
#     return render(request,'addbooks.html')

class Home(View):
    def get(self,request):
      return render(request,'home.html')


class Viewbooks(View):
    def get(self,request):
        b=Book.objects.all()
        context={'books':b}
        return render(request,'viewbooks.html',context)


class Addbooks(View):
    def get(self,request):
        form_instance=Addbookforms()
        context={'form':form_instance}
        return render(request,'addbooks.html',context)



    def post(self,request):
        form_instance = Addbookforms(request.POST,request.FILES)
        if form_instance.is_valid():
            # data = form_instance.cleaned_data
            # print(data)
            # title =data['title']
            # author = data['author']
            # price = data['price']
            # pages = data['pages']
            # language = data['language']

            # b=Book.objects.create(title=title,author=author,price=price,page=pages,language=language)
            # b.save()
            form_instance.save()
            context={'form':form_instance}
            # context = {'t':title,'a':author,'p':price,'page':pages,'l':language}
            return render(request, 'addbooks.html',context)

class Detail(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        context={'book':b}

        return render(request,'detail.html',context)
    def post(self,request):
        pass


class Edit(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=Addbookforms(instance=b)
        context={'form':form_instance}

        return render(request,'edit.html',context)
    def post(self,request,i):

            b = Book.objects.get(id=i)

            form_instance = Addbookforms(request.POST, request.FILES,instance=b)
            if form_instance.is_valid():
                form_instance.save()


                return redirect('books:viewbooks')




class Delete(View):
        def get(self,request,i):
              b=Book.objects.get(id=i)
              b.delete()
              return redirect('books:viewbooks')

        def post(self, request):
            pass




