from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
     path('book/<int:book_id>/', views.book_details, name='book_details'),
    

    path('accounts/login/', LoginView.as_view(), name='login'),

   
]

