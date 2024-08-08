from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('', views.home, name='home'),
    path('thread/<str:pk>/', views.thread, name='thread'),
    path('create-thread/', views.createThread, name='create-thread'),
    path('update-thread/<str:pk>/', views.updateThread, name='update-thread'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

]