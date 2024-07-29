from django.urls import path
from .views import *



#http://127.0.0.1:8000/lms/home/

urlpatterns = [
    
    path('home/',view_home,name='home'),  
    path('login/',view_login,name='login'),
    path('logout/',view_logout,name='logout'),
    path('register/',view_register1,name='register'),
    path('secure1/',view_secure1,name='secure1'),
    path('secure2/',view_secure2,name='secure2'),
    path('unsecure1/',view_unsecure1,name='unsecure1'),
    path('unsecure2/',view_unsecure2,name='unsecure2'),
    
    


    
]