from django.shortcuts import render


#
# def addition(request):
#     if(request.method=="GET"):
#         return render(request,'addition.html')
#     if (request.method=="POST"):
#         print(request.POST)
#         n1=request.POST('num1')
#
#         s=fact*num1
#         context={'result':s,'n1':n1}
#         return render(request, 'addition.html')

def addition(request):
    if(request.method=="GET"):
          return render(request,'addition.html')

    if(request.method=="POST"):   # After form submission
        print(request.POST)
        n1=request.POST['num1']
        n2=request.POST['num2']
        s=int(n1)+int(n2)

        context={'result':s,'num1':n1,'num2':n2}
        return render(request,'addition.html',context)




def factorial(request):
    if(request.method=="GET"):
        return render(request,'factorial.html')
    if(request.method=="POST"):
        print(request.POST)
        n=int(request.POST['num'])
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        context={'result':fact,'num':n}
        return render(request,'factorial.html',context)



# def bmi(request):
#     if(request.method=="GET"):
#         return render(request,'bmi.html')
#     if(request.method=="POST"):
#         print(request.POST)
#         wt=float(request.POST['wt'])
#         ht=float(request.POST['ht'])
#         ht=ht/100
#         r=(wt/(ht**2))
#         context={'result':r,'ht':ht,'wt':wt}
#         return render(request,'bmi.html',context)

