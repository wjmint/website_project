from django.urls import path
from base import views

# template tagging
app_name = 'base'

urlpatterns = [
    path('others/', views.others, name='others'),
    path('relative/', views.relatives, name='relatives'),
]