import uuid
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