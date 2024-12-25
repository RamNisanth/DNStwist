from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # path('/login', views.login, name='login'),  # Example route
    # path('/register', views.register, name='register'),  # Example route
    path('register/', views.register, name='register'),
    path('login/', views.login.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]
