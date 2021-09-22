from django.conf.urls import url
from django.urls import path
from .views import StudentCreateView, SchoolDetailCreateView, SchoolDetailUpdateView,SchoolListView, SchoolDetailView, SchoolDeleteView, StudentCreateView


app_name = 'basic_app'
urlpatterns = [
    path('', SchoolListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',SchoolDetailView.as_view(),name='detail'),
    url(r'^create/$',SchoolDetailCreateView.as_view(),name='create'),
    url(r'^update(?P<pk>[-\w]+)/$',SchoolDetailUpdateView.as_view(),name='update'),
    url(r'delete(?P<pk>[-\w]+)/$', SchoolDeleteView.as_view(), name = 'delete'),
    url(r'^stdcreate/$',StudentCreateView.as_view(),name='stdcreate'),    
]