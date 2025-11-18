from django.shortcuts import render
from django.views import View
from app1.forms import Additionform,Factorialform,Bmiform,Signupform
class Addition(View):
    def get(self,request):
        form_instance=Additionform()
        context={'form':form_instance}
        return render(request,'addition.html',context)
    def post(self,request):
        # cresting form objects using submitted data
        form_instance=Additionform(request.POST)
        # check whether data is valid or not
        if form_instance.is_valid():
            #process the data after validation
            data=form_instance.cleaned_data
  8          print(data)
            n1=data['num1']
            n1=data['num2']
            s=int(n1)+int(n2)
            context={'result':s,'form':form_instaance}

            return render(request,'addition.html')


class Factorial(View):
    def get(self,request):

        form_instance=Factorialform()

        context={'form':form_instance}
        return render(request,'factorial.html',context)

    def post(self,request):

        form_instance=Factorialform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            n=data['num']
            fact=1
            for i in range(1,n+1):
                fact=fact*i
            context={'result':fact}
            return render(request, 'factorial.html')


class Bmi(View):
    def get(self,request):
        form_instance=Bmiform()
        context={'form':form_instance}
        return render(request,'bmi.html',context)

    def post(self,request):
        form_instance = Bmiform(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            wt=data['weight']
            ht=data['height']

            b=(wt/(ht**2))
            context={'result':b,'form':form_instance}
            return render(request, 'bmi.html')


class Signup(View):
    def get(self,request):
        form_instance=Signupform()
        context={'form':form_instance}
        return render(request,'signup.html',context)

    def post(self,request):
        form_instance = Signupform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            username=data['username']
            password = data['password']
            email = data['email']
            phone = data['phone']
            address = data['address']
            gender = data['gender']
            role = data['role']
            context = {'user':username,'pass':password,'email':email,'phone':phone,'address':address,'gender':gender,'role':role}
            return render(request, 'signup.html')

