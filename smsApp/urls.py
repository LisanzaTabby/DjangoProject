from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    #path('signup/', views.signup, name='signup'),
    #path('signin/', views.signin, name='signin'),
    path('student/', views.student, name='student'),
    path('edit/<str:pk>/', views.edit, name='edit')
    #path('signout', views.signout, name= 'signout'),
]