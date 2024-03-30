from django.db import models

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    Book_Title = models.CharField(max_length=255)
    Book_Author = models.CharField(max_length=255)
    Year_Of_Publication = models.IntegerField()
    Publisher = models.CharField(max_length=255)
    Image_URL_S = models.URLField()
    Image_URL_M = models.URLField()
    Image_URL_L = models.URLField()

    def __str__(self):
        return self.Book_Title
