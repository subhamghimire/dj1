
from django.urls import path
from . import views
urlpatterns = [
path('',views.homepage),
path('countsss/',views.count,name='count')
]
