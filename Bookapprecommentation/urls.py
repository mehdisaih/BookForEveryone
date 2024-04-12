from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,),
    path('books', views.books),
    path('about', views.about),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('book/',include('book.urls'),name="book"),

]