from django.urls import path
from .views import (
    list_view, 
    #Work exercise ,Insert code here
    join   #new function in  views.py
)

app_name = 'main'
urlpatterns = [
    path('', list_view, name='home-list'),    
    #Work exercise ,Insert code here
    path('join-now',join, name='hangout'),#new url route
]