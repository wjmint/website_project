from django.contrib import admin
from django.conf.urls import url    
from django.urls import path
from .views import SchoolDetailDeleteView, SchoolDetailUpdateView, SchoolListView, SchoolDetailView


app_name = 'basic_app'
urlpatterns = [
    path('', SchoolListView.as_view(), name='list'),
    url(r'(?P<pk>[-\w]+)/',SchoolDetailView.as_view(),name='detail'),
    url(r'^update(?P<pk>\d+)/$', SchoolDetailUpdateView.as_view(), name='update'),
    # url(r'^delete(?P<pk>\d+)/$', SchoolDetailDeleteView.as_view(), name='delete')
    
]