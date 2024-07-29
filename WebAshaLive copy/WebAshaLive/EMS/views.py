from django.shortcuts import render
from django.http import HttpResponse
from EMS.models import Employee    #to import model from models.py in insertems.html view

# Create your views here.

# class Employee:
#     def __init__(self):
#         self.name=""
#         self.age=0
#         self.address=""
#         self.mobileno=""
#         self.post=""
#         self.salary=0

# def get_N_Employee(n):
#     empList=[]
#     for i in range(1,n+1):
#         emp=Employee()
#         emp.name="Rupali Gurav"+str(i)
#         emp.age=26+i
#         emp.address='Pune'+str(i)
#         emp.mobileno='78912389'+str(i)
#         emp.post='SE'+str(i)
#         emp.salary=78945625.23+i
#         empList.append(emp)

#     return empList



# def view_home(request):
#     if request.method=="GET":
#         resp=render(request,'ems/home.html')
#         return resp
    
#     elif request.method=="POST":

#         empno=int(request.POST.get('txtNo',0))


#         employees=get_N_Employee(empno)
#         d1={'employees':employees}
#         resp=render(request,'ems/home.html',context=d1)
#         return resp


def rupali_google(request):
    resp=HttpResponse('<h1> Hello I am Google </a> </h1>')
    return resp


def view_insert_ems(request):
    if request.method == 'GET':
        resp = render(request,'EMS/insertems.html')
        return resp
    if request.method == 'POST':
        if 'btnaddemp' in request.POST:
            emp1 = Employee()
            emp1.name = request.POST.get('txtname','NA')    #in get name of the input 'txtname'
            emp1.age= request.POST.get('txtage',0)
            emp1.mobileno = request.POST.get('txtmob','NA')
            emp1.address = request.POST.get('txtadd','NA')
            emp1.save()
            resp = HttpResponse("<h1 bgcolor='green'>Successfully submitted</h1>")
            return resp
        
        elif 'btnsearch' in request.POST:
            eid = int(request.POST.get('txtid',0))    #Take id from frontend and searches in database
            emp1 = Employee()
            emp1 = Employee.objects.get(id = eid)     #manager object is get   and matches id to client id
            d1 = {'emp' : emp1}
            resp = render(request,'EMS/insertems.html',context=d1)
            return resp
        
        elif 'btnupdate' in request.POST:
            emp = Employee()
            emp.id = int(request.POST.get('txtid',0))
            if Employee.objects.filter(id = emp.id).exists():
                emp.name = request.POST.get('txtname','NA')
                emp.age= request.POST.get('txtage')
                emp.mobileno = request.POST.get('txtmob','NA')
                emp.address = request.POST.get('txtadd','NA')
                emp.save()
                resp = HttpResponse("<h1 bgcolor='green'>Successfully updated</h1>")
                return resp
            
        elif 'btndelete' in request.POST:
            emp1 = Employee()
            emp1.id = int(request.POST.get('txtid',0))
            Employee.objects.filter(id = emp1.id).delete()
            resp = HttpResponse("<h1 bgcolor='green'>Successfully deleted</h1>")
            return resp
        
        elif 'btnsearchall' in request.POST:
            allemp1 = Employee.objects.all()    #manager object is all
            d1 = {'allemp' : allemp1 }
            resp = render(request,'EMS/insertems.html',context=d1)
            return resp
        


        
        









