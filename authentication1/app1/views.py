from django.shortcuts import render,redirect
from django.views import View
from app1.forms import SignupForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Register(View):
    def get(self,request):
        form_instance = SignupForm()
        context = {'form': form_instance}
        return render(request,'register.html',context)
    def post(self,request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('userlogin')
        else:
            print(form_instance.errors)

class Userlogin(View):
    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'login.html',context)

    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data   # fetches data after validation
            u=data['username']            # retrieves username from cleaned data
            p=data['password']            # retrieves password from cleaned data
            user=authenticate(username=u,password=p)      # calls authenticate() to verify if user exist
                                                          # if record exists then it returns user object
                                                          # else none
            if user:      # if user exists
                login(request,user)        # adds the user into current session
                return redirect('home')

            else:     # if user deos not exists
                messages.error(request, "Invalid Credentials")

                return redirect('userlogin')

class Userlogout(View):
    def get(self,request):
        logout(request)  #remove the user from the session
        return redirect('home')



