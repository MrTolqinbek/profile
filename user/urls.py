from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logoutPage, name='logout'),
    path('accaunt/', views.userAccaunt, name='accaunt'),
    path('login/', views.LoginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.profile, name='profile'),
]
