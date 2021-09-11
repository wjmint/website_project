from django.contrib import admin
from django.conf.urls import url    
from django.urls import path
from .views import SchoolListView, SchoolDetailView


app_name = 'basic_app'
urlpatterns = [
    path('', SchoolListView.as_view(), name='list'),
    url(r'(?P<pk>[-\w]+)/',SchoolDetailView.as_view(),name='detail'),
    
]