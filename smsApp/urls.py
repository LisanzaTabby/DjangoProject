from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    #path('add_user/', views.add_user, name='add_user'),
    path('users/', views.list_users, name='list_users'),
    path('edit/', views.edit, name='edit'),
    path('signout', views.signout, name= 'signout'),
]