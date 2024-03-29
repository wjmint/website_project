from os import name
from django.urls import path
from basic import views

app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name = 'user_login'),
    path('userinfo/', views.user_info, name = 'user_info')
]