from django.db import models


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
