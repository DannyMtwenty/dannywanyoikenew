from django.urls import path
from myportfolio.views import *

urlpatterns = [
    path('',home,name="home"),
    path('contact',contact, name='contact'),
]
