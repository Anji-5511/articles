from django.urls import path
from .import views

urlpatterns = [
    path('1',views.home,name='index'),
    path('one/<int:pk>',views.navigate,name='navigate'),
]
