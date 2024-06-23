from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< Updated upstream
     path('book/<int:book_id>/', views.book_details, name='book_details'),
    

    path('accounts/login/', LoginView.as_view(), name='login'),

   
]

=======
    path('make_purchase/', views.make_purchase, name='make_purchase'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('addtocart/', views.addtocart,name="addtocart"),
    path('cart/', views.cart,name="cart"),
    path('removefromcart/<int:id>', views.removefromcart,name="removefromcart"),
    path('addquantity/<int:id>/<int:quantity>', views.addquantity,name="addquantity"),
    path('removequantity/<int:id>/<int:quantity>', views.removequantity,name="removequantity"),
]
>>>>>>> Stashed changes
