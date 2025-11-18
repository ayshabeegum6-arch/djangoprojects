from django.shortcuts import render,redirect
from django.views import View
from app1.forms import SignupForm,LoginForm
from django.contrib.auth import authentication,login,logout
from django.contrib import messages




class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('userlogin')

    def get(self,request):
        form_instance = SignupForm()
        context={'form':form_insttance}
        return render(request,'register.html',context)

class Userlogin(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        form_instance=loginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data  #fetaches data after validation
            u=data['username'] #retrives username from cleaned_data
            p=data['password']  #retrieves password from cleaned data
            user=authenticate(username=u,password=p)

            if user:
                login(request,user)
                return redirect('home')
            else: #if user doesnot exist
                print('invalid credentials')
                reurn redirect('login')

class Userlogout(View):
    def get(self,request):

        return redirect('userlogin')
