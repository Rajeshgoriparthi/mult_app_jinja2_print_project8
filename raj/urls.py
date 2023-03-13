from raj.views import *
from django.urls import path
app_name='some'
urlpatterns=[
    path('friends/',friends,name='friends'),
]