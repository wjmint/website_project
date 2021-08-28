from django.contrib import admin
from django.urls import path
from .views import views

app_name = 'basic_app'
urlpatterns = [
    path('list', views.SchoolListView.as_view(), name='list')
]