from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),

path('base/',views.base,name='base'),
path('base/add',views.add,name='add'),
path('update/<str:pk>/',views.update,name='update'),
path('register', views.register, name='register'),
path('delete/<str:pk>/', views.delete, name='delete'),

]