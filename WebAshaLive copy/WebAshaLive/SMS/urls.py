from django.urls import path
from .views import *


# http://127.0.0.1:8000/sms/payment/
urlpatterns = [
    path('payment/',view_student_wise_paymentDetails),
    path('course/',view_course_wise_Students),
    path('stufrm/',view_student_frm),
    path('payfrm/',view_PaymentDetails_frm),
    path('statics/',view_static_file_example),
   
]
