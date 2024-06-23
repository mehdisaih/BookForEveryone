from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path,include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,),
    path('books', views.books),
    path('about', views.about),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('logout/', views.logout,name="logout"),
    path('user/', views.default),
    path('book/',include('book.urls'),name="book"),
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    

    path('book/<int:book_id>/', views.book_details, name='book_details'),
    # URL pour ajouter un article au panier
    


]
