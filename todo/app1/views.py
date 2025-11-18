from django.shortcuts import render,redirect
from django.views import View
from app1.forms import AddTaskForms
from app1.models import Todo




class Home(View):
    def get(self, request):
        form_instance = AddTaskForms()
        t=Todo.objects.all()
        context = {'form1': form_instance,'Todo':t}
        return render(request, 'home.html', context)

    def post(self, request):
        form_instance = AddTaskForms(request.POST)

        if form_instance.is_valid():
            form_instance.save()

            form_instance = AddTaskForms()
            t = Todo.objects.all()

            context = {'form1': form_instance,'Todo':t}
            return render(request, 'home.html', context)






class Edit(View):
    def get(self,request,i):
        t=Todo.objects.get(id=i)
        form_instance=AddTaskForms(instance=t)
        context={'form':form_instance}

        return render(request,'edit.html',context)
    def post(self,request,i):

            t = Todo.objects.get(id=i)

            form_instance = AddTaskForms(request.POST, instance=t)
            if form_instance.is_valid():
                form_instance.save()


                return redirect('home')



class Delete(View):
    def get(self, request, i):
        t= Todo.objects.get(id=i)
        t.delete()
        return redirect('home')