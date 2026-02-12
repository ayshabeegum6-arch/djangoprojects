from django.shortcuts import render,redirect
from django.views import View
from app1.forms import SignupForm,LoginForm,SchoolForm,Studentform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from app1.models import Student,School
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')




class Register(View):
    def get(self,request):
        form_instance = SignupForm()
        context = {'form': form_instance}
        return render(request,'register.html',context)

    def post(self, request):
       form_instance = SignupForm(request.POST)
       if form_instance.is_valid():

        # save the user but not commit
            user = form_instance.save(commit=False)
            role = form_instance.cleaned_data['role']

        # Admin registration
            if role == 'admin':
                user.is_superuser = True
                user.is_staff = True
            user.save()

        # Student registration
            if role == 'student':
              Student.objects.create(
                user=user,
                name=form_instance.cleaned_data['first_name'])


            messages.success(request, "User registered successfully!")
            return redirect('userlogin')

       return render(request, 'register.html', {'form': form_instance})


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


class Addschool(View):
    def get(self, request):
        form_instance = SchoolForm()
        return render(request, 'addschool.html', {'form': form_instance})

    def post(self, request):
        form_instance = SchoolForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            messages.success(request, "School added successfully")
            return redirect('schoollist')

        return render(request, 'addschool.html', {'form': form_instance})


class SchoolList(View):
    def get(self, request):
        data = School.objects.all()
        return render(request, 'schoollist.html', {'data': data})


class Schooldetail(View):
    def get(self, request, i):
        s=School.objects.get(id=i)
        u=request.user
        can_join=True
        is_student=False
        try:
            stu=Student.objects.get(user=u)
            can_join=False
            if stu.school==s:
                is_student=True
        except:
            pass
        print(can_join,is_student)
        # data = School.objects.get(id=i)
        context={'school':s,'can_join':can_join,'is_student':is_student}
        return render(request, 'schooldetail.html',context)

class Studentjoin(View):
    def get(self, request, i):
        form_instance = Studentform()
        context={'form':form_instance}
        return render(request, 'studentjoin.html',context)

    def post(self, request, i):
        s = School.objects.get(id=i)   # selected school
        u = request.user               # logged-in user
        form_instance = Studentform(request.POST)
        if form_instance.is_valid():
            stu = form_instance.save(commit=False)
            stu.schoolname = s        # correct field name
            stu.user = u
            stu.save()
            return render(request,'schoollist.html')

class Delete(View):
    def get(self,request,i):
     u=request.user
from django.shortcuts import render,redirect
from django.views import View
from app1.forms import SignupForm,LoginForm,SchoolForm,Studentform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from app1.models import Student,School
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')




class Register(View):
    def get(self,request):
        form_instance = SignupForm()
        context = {'form': form_instance}
        return render(request,'register.html',context)

    def post(self, request):
       form_instance = SignupForm(request.POST)
       if form_instance.is_valid():

        # save the user but not commit
            user = form_instance.save(commit=False)
            role = form_instance.cleaned_data['role']

        # Admin registration
            if role == 'admin':
                user.is_superuser = True
                user.is_staff = True
            user.save()

        # Student registration
            if role == 'student':
              Student.objects.create(
                user=user,
                name=form_instance.cleaned_data['first_name'])


            messages.success(request, "User registered successfully!")
            return redirect('userlogin')

       return render(request, 'register.html', {'form': form_instance})


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


class Addschool(View):
    def get(self, request):
        form_instance = SchoolForm()
        return render(request, 'addschool.html', {'form': form_instance})

    def post(self, request):
        form_instance = SchoolForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            messages.success(request, "School added successfully")
            return redirect('schoollist')

        return render(request, 'addschool.html', {'form': form_instance})


class SchoolList(View):
    def get(self, request):
        data = School.objects.all()
        return render(request, 'schoollist.html', {'data': data})


class Schooldetail(View):
    def get(self, request, i):
        s=School.objects.get(id=i)
        u=request.user
        can_join=True
        is_student=False
        try:
            stu=Student.objects.get(user=u)
            can_join=False
            if stu.school==s:
                is_student=True
        except:
            pass
        print(can_join,is_student)
        # data = School.objects.get(id=i)
        context={'school':s,'can_join':can_join,'is_student':is_student}
        return render(request, 'schooldetail.html',context)

class Studentjoin(View):
    def get(self, request, i):
        form_instance = Studentform()
        context={'form':form_instance}
        return render(request, 'studentjoin.html',context)

    def post(self, request, i):
        s = School.objects.get(id=i)   # selected school
        u = request.user               # logged-in user
        form_instance = Studentform(request.POST)
        if form_instance.is_valid():
            stu = form_instance.save(commit=False)
            stu.schoolname = s        # correct field name
            stu.user = u
            stu.save()
            return render(request,'schoollist.html')

class Delete(View):
    def get(self,request,i):
     u=request.user
