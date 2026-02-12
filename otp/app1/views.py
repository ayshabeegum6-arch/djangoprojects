from django.shortcuts import render,redirect
from django.views import View
from app1.forms import SignupForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from app1.models import CustomUser
# Create your views here.
from django.core.mail import send_mail
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
            u=form_instance.save(commit=False)
            u.is_active=False  #is_active default value is true
            u.save()
            u.generate_otp()  #calls generate_otp  is defined in model
            send_mail(
                "Django Auth OTP",
                u.otp,
                "sandhraeldhose37@gmail.com",
                [u.email],
                fail_silently=False,
            )

            return render(request,'verify.html')
        # else:
        #     print(form_instance.errors)
            # If form is invalid, re-render the same form with errors
            # context = {'form': form_instance}
            # return render(request, 'register.html',context)



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
            if user and user.is_superuser==True:      # if user exists
                login(request,user)        # adds the user into current session
                return render(request,'adminhome.html')
            elif user and user.role=="student":
                login(request,user)
                return render(request,'studenthome.html')
            elif user and user.role == "teacher":
                login(request, user)
                return render(request,'teacherhome.html')

            else:     # if user deos not exists
                messages.error(request, "Invalid Credentials")

                return redirect('userlogin')

class Userlogout(View):
    def get(self,request):
        logout(request)  #remove the user from the session
        return redirect('userlogin')


class Otpverify(View):
    def get(self,request):
        return redirect(request,'verify.html')

    def post(self,request):
        o=request.POST['o']               #retrieve the otp send by user
        u=CustomUser.objects.get(otp=o)   #checks whether record matching with entered otp exists
                                           #if exists then
        u.is_active=True                  #enabling user to login in
        u.is_verified=True               #sets is_verified to True
        u.otp=None                      # clear the otp from table
        u.save()                           # saves the data
        return render(request,'login.html')



