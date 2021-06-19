from django.urls import path
from basic import views

app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register')
]