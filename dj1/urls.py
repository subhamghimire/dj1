
from django.urls import path
from . import views
urlpatterns = [
path('',views.homepage),
path('countss/',views.count,name='count')
]
