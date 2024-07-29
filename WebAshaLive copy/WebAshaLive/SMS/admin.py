from django.contrib import admin
from SMS.models import *
# Register your models here.

# 1. Method One:

# admin.site.register(Student)      # Only shows name by default due to __str__ method defined while model creating


@admin.register(Student)     #predefined decorator in system
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','mobileno','dob','pic']


# admin.site.register(Course) 

@admin.register(Course)     #predefined decorator in system
class CourseAdmin(admin.ModelAdmin):
    list_display=['id','name']


# admin.site.register(PaymentDetails) 

@admin.register(PaymentDetails)     #predefined decorator in system
class PaymentAdmin(admin.ModelAdmin):
    list_display=['id','amount','payment_mode','student']



