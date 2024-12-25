from django.urls import path
from . import views

urlpatterns = [
    # path('/permutations', views.permutations, name='permutations'),  # Example route
    path('service/', views.myservice, name='myservice'),
    path('option1/', views.option1, name='option1'),
    path('option2/', views.option2, name='option2'),
    path('option3/', views.option3, name='option3'), 
    path('download_page/', views.download_page, name='download_page'),
]
