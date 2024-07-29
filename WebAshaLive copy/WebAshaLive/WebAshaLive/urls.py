"""
URL configuration for WebAshaLive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.shortcuts import render


def view_sum(request,a,b):
    return HttpResponse("<h1>Hello I am calling sum="+str(a+b)+"</h1>")

def view_sub(request,i,j):
    return HttpResponse("<h2>Hello I am calling subtract="+str(i-j)+"</h2>")


def name(request):
    return HttpResponse("<h1>Hello Rupali! How are you</h1>")

def view_multi(request,a,b):
    return HttpResponse("<h1>Hello I am calling Multiply="+str(a*b)+"</h1>")

def view_div(request,a,b):
    return HttpResponse("<h1>Hello I am calling Divide="+str(a/b)+"</h1>")

def view_exp(request,a,b):
    return HttpResponse("<h1>Hello I am calling Exponent="+str(a**b)+"</h1>")

def view_calc(request):
    a=int(request.POST.get('t1',0))
    b=int(request.POST.get('t2',0))
    #c=int(request.POST.get('t3',0))

    if request.method=='GET':
        resp=render(request,'calculator.html')
        return resp

    if 'btnsum' in request.POST:
        
        c=a+b
        #d1={'a':a,'b':b,'c':c}
    #print('a=',a,'b=',b,'c=',c)
        #resp=render(request,'calculator.html',context=d1)
        #return resp
    
    elif 'btnsub' in request.POST:
        c=a-b
        #d1={'a':a,'b':b,'c':c}
        #resp=render(request,'calculator.html',context=d1)
        #return resp
    
    elif 'btnmult' in request.POST:
        c=a*b
        #d1={'a':a,'b':b,'c':c}
        #resp=render(request,'calculator.html',context=d1)
        #return resp
    
    elif 'btndiv' in request.POST:
        c=a/b
    d1={'a':a,'b':b,'c':c}
    resp=render(request,'calculator.html',context=d1)
    return resp


def view_calc2(request):
    a=int(request.POST.get('txtFirst',0))
    b=int(request.POST.get('txtSecond',0))
    if request.method=='GET':
        resp=render(request,'calc.html')
        return resp
    elif request.method == 'POST':
        if 'btnsum' in request.POST:
            c=a+b
        d1={'a':a,'b':b,'c':c}
    resp=render(request,'calc.html',context=d1)
    return resp

    


    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/<int:a>/<int:b>/',view_sum),
    path('sub/<int:i>/<int:j>/',view_sub),
    path('multi/<int:a>/<int:b>/',view_multi),
    path('rupali/',name),
    path('div/<int:a>/<int:b>/',view_div),
    path('exp/<int:a>/<int:b>/',view_exp),
    path('calc/',view_calc),
    path('calc2/',view_calc2),
    path('ems/',include('EMS.urls')),  # http://127.0.0.1:8000/ems/
    path('sms/',include('SMS.urls')),  # http://127:0.0.1:8000/sms/
    path('lms/',include('LMS.urls')),  #http://127.0.0.1:8000/lms/
    path('demoapi/',include('demoapi.urls')),

]
