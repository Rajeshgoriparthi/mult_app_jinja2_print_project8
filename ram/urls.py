from ram.views import *
from django.urls import path
app_name='some'
urlpatterns=[
    path('best_friends/',best_friends,name='best_friends'),
]