from SMS.models import *    # import data from models to access here in views
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.






#PAyment details rcord after entering id of student
#----------->>>>> 1.----------------------------->>>>>>
def view_student_wise_paymentDetails(request):
    # to render page on browser get method
    if request.method=="GET":

        # return for get request
        resp=render(request,'SMS/PaymentDetails.html')
        return resp
    
    # post method to access data and return to client
    elif request.method=='POST':
        sid=int(request.POST.get('txtId',0))    #name of enter id in html to access
        
        s1=Student.objects.get(id=sid)   #from student table get the dada that user enetred match that

        allp=s1.paymentdetails_set.all()  # paymentdetails_set : it is a related manager that django creats to access all payment details related to that particular student #.all() : its a method called on previous manager to retrive all payment details of that student  
        #print('ALLP=',allp)
        #Made a dictionary so that through this key data can be accessed in frontend via loop
         #payments key will be accessed in dtl in html  #stu is key to access student in for loop
         #id is key to retain the id of student that user entered in input

        d1={'payments':allp,'stu':s1,'id':sid}   
        # return for post request 
        resp=render(request,'SMS/PaymentDetails.html',context=d1)
        return resp
    





# Course wise student data retriving from database
#------------------------------------------------->>>>>>
def view_course_wise_Students(request):
    
    # allcourse and d1 made global so that it can access all course data
    # Here is one dictionary and has multiple keys that's why context is d1 in get and post request
    # Making a key to access data
    allcourse=Course.objects.all()
    d1={'courses':allcourse}

    if request.method=='GET':
        # To keep default python that is why id =1 
        c=Course.objects.get(id=1)
        d1['cid']=c.id
        d1['cname']=c.name
        allstu=c.student.all()
        # d1={'students':allstu}
        d1['students']=allstu
        resp=render(request,'SMS/course.html',context=d1)
        return resp
    
    elif request.method=="POST":
        cid=int(request.POST.get('txtid',0)) #txtid select tag name
        # matching cid with get course id from database 
        c=Course.objects.get(id=cid)
        # it is to match the cid with c.id and cname with c.name --->>user input == database entry
        d1['cid']=c.id
        d1['cname']=c.name
        # it has many to many relationship student is variable in course class that cooncets both so we are retriving all students that has taken a particular course. that is why allstu holds all students of that course
        allstu=c.student.all()
        # matching and making a key students to hold allstu 
        d1['students']=allstu
        resp=render(request,'SMS/course.html',context=d1)
        return resp
    



    
def view_student_frm(request):
    if request.method=='GET':
        frm_unbound=StudentForm()   # unbound means without data
        d1={'forms':frm_unbound}
        resp=render(request,'SMS/stufrm.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=StudentForm(request.POST)
        if frm_bound.is_valid():  # server side validation
            frm_bound.save()
            resp=HttpResponse("<h1>Student Registered SuccessFully!</h1>")
            return resp
        else:
            d1={'forms':frm_bound}
            resp=render(request,'SMS/stufrm.html',context=d1)
            return resp
        
def view_PaymentDetails_frm(request):
    if request.method == 'GET':
        frm_unbound = PaymentDetailsForm()
        d1 = {'form':frm_unbound}
        resp = render(request,'SMS/payfrm.html',context=d1)
        return resp
    elif request.method == 'POST':
        frm_bound = PaymentDetailsForm(request.POST)   
        if frm_bound.is_valid():   #Sever side validation
            frm_bound.save()
            resp = HttpResponse("<h1>Payment Done Successfully</h1>")
            return resp   #Attention
        else:
            d1 = {'form':frm_bound}
            resp = render(request,'SMS/payfrm.html',context = d1)
            return resp
        

def view_static_file_example(request):
    resp = render(request,'SMS/statics.html')
    return resp

        




