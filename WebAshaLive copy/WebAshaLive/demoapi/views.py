from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from SMS.models import Student
from .serialize import StudentSerializer
# Create your views here.

# @api_view(['GET','POST','DELETE','PUT'])
# # @api_view(http_method_names=['GET','POST'])
# def view_firstapi(request):
#     a = {'M':'m','r':'r','s':'s'}
#     resp = Response(data=a)
#     return resp

@api_view(['GET','POST'])
# @api_view(http_method_names=['GET','POST'])
def view_firstapi(request,sid):
    
    stu = Student.objects.get(id=sid)
    stu_serialize = StudentSerializer(stu).data
    resp = Response(data=stu_serialize)
    return resp









