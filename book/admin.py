from django.contrib import admin
from .models import Final_Rating

class Final_RatingAdmin(admin.ModelAdmin):
    list_display = ('User_ID', 'ISBN', 'Rating', 'Title', 'Author', 'Year', 'Publisher', 'Image_URL_L', 'num_of_rating')
    search_fields = ['User_ID', 'ISBN', 'Title', 'Author', 'Publisher']  # Add fields you want to search on

admin.site.register(Final_Rating, Final_RatingAdmin)
