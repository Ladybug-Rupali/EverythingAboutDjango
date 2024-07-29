from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .decorator import is_CheckloginorRegister
from django.contrib.auth.decorators import login_required






# Create your views here.



def view_home(request):
    resp1 = render(request,'LMS/home.html')
    return resp1
    




@is_CheckloginorRegister
def view_register1(request):
    if request.method=='GET':
        frm_unbound=UserCreationForm()
        d1={'forms':frm_unbound}
        resp=render(request,'LMS/register1.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=UserCreationForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            

            resp=HttpResponse("<h1>User created successfully!</h1>")
            return resp
        else:
            d1={'forms':frm_unbound}
            resp=render(request,'LMS/register1.html',context=d1)
            return resp
   
       
        


            


        

   

@is_CheckloginorRegister
def view_login(request):
    
    if request.method == "GET":

        resp = render(request,'LMS/login.html')
        return resp
    
    elif request.method == "POST":
        u_name = request.POST.get('txtuser','NA')
        u_password = request.POST.get('txtpsw','NA')

        user = authenticate(request,username=u_name,password=u_password)

        if user is not None:
            login(request,user)
            # resp = HttpResponse("<h1>Logged in successfully!</h1>")
            # return resp
            resp = render(request,'LMS/home.html')
            return resp
        else:
            resp = render(request,'LMS/home.html')
            return resp
        

def view_logout(request):
    logout(request=request)
    return render(request,'LMS/logout.html')



   




        

        





@login_required(login_url='login')
def view_secure1(request):
    resp = render(request,'LMS/secure1.html')
    return resp

@login_required(login_url='login')
def view_secure2(request):
    resp = render(request,'LMS/secure2.html')
    return resp


def view_unsecure1(request):

    resp = render(request,'LMS/unsecure1.html')
    return resp


def view_unsecure2(request):
    resp = render(request,'LMS/unsecure2.html')
    return resp






