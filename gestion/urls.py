from django.contrib import admin
from django.urls import path,include
from gestion import views

urlpatterns = [
path('',views.home, name='home'),
path('login/',views.login_view, name='login'),
path('signup/',views.signup, name='signup'),
path('logout/', views.logout_view, name='logout'),

]
