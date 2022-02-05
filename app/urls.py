from django.urls import path  
from . import views

urlpatterns= [
	path('',views.home,name="home") ,
	path('create/', views.create, name='create'),
	path('update/<str:id>/', views.update, name='update'),
    path('read/<str:id>/', views.read, name='read'), #read/1/
    path('delete/<str:id>/', views.delete, name='delete'),

]