import uuid
from django.db import models
from django.contrib.auth.models import User
<<<<<<< Updated upstream
=======
 

>>>>>>> Stashed changes

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
    
<<<<<<< Updated upstream
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
    

=======
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
            return self.user.username

    @property
    def total_price(self):
        cartitems = self.cartitem.all()
        total = sum([book.price for book in cartitems])
        return total
    
    @property
    def num_of_items(self):
        cartitems = self.cartitem.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity
    

class cartitems(models.Model):
    Final_Rating=models.ForeignKey(Final_Rating,on_delete=models.CASCADE,related_name="Final_Rating") 
    cart= models.ForeignKey(Cart ,on_delete=models.CASCADE,related_name="cartitem")  
    quantity=models.IntegerField(default=0)  
    
    def __str__(self):
        return str(self.Final_Rating.Title)  

    @property
    def price(self):
        return self.Final_Rating.num_of_rating*self.quantity    


>>>>>>> Stashed changes
