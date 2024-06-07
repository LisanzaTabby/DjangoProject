from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    #path('signup/', views.signup, name='signup'),
    #path('signin/', views.signin, name='signin'),
    path('users/<str:pk_test>/', views.list_users, name='list_users'),
    path('edit/<str:pk>/', views.edit, name='edit')
    #path('signout', views.signout, name= 'signout'),
]