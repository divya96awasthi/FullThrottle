from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),    # url for homepage
    path('json_file/', views.json_generator,name='json_file')   # url to generate json data
]