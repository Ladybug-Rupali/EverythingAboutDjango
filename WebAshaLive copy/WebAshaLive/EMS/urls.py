from django.urls import path
from .views import *



# BASE URL==> http://127.0.0.1:8000/ems/
urlpatterns = [
    #path('home/',view_home),  #http://127.0.0.1:8000/ems/home/
    #path('google/',rupali_google),
    path('emshm/',view_insert_ems),
]
