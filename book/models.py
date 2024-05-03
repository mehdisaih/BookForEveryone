from django.db import models
from django.contrib.auth.models import User

class Final_Rating(models.Model):
    User_ID = models.IntegerField()
    ISBN = models.CharField(max_length=255)
    Rating = models.IntegerField()
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Year = models.IntegerField()
    Publisher = models.CharField(max_length=255)
    Image_URL_L = models.CharField(max_length=255)
    num_of_rating=models.IntegerField()

    class Meta:
        app_label = 'book' 

    def __str__(self):
        return str(self.User_ID)
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name} in cart for {self.cart.user.username}"
    

