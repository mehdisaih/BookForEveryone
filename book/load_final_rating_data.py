import os
import django
import sys
import pickle
import pandas as pd


# Modify the sys.path to include the directory containing your Django project
sys.path.append('C:\\Users\\dell\\Desktop\\BookForEveryone')

# Replace 'myproject.settings' with the actual path to your Django project's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bookapprecommentation.settings')

# This is required to set up Django
django.setup()

from book.models import Final_Rating  # Import your Django model after django.setup()

def load_final_rating_data():
    try:
        from django.conf import settings
        from django.core.exceptions import ImproperlyConfigured

        # Check if INSTALLED_APPS is defined in settings
        if not settings.configured:
            raise ImproperlyConfigured("Django settings are not properly configured.")

        # Now you can access Django models safely
        from Bookapprecommentation.settings import BASE_DIR

        with open(os.path.join(BASE_DIR, 'C:\\Users\\dell\\Desktop\\BookForEveryone\\Model\\artifacts\\final_rating.pkl'), 'rb') as file:
            final_rating_data = pickle.load(file)
            print("Final rating data:", final_rating_data)  # Print final_rating_data for debugging

            print(final_rating_data)

            if isinstance(final_rating_data, pd.DataFrame):
                for index, row in final_rating_data.iterrows(): # Print the record dictionary
                    final_rating_obj = Final_Rating(
                    User_ID=row['User-ID'],
                    ISBN=row['ISBN'],
                    Rating=row['Rating'],
                    Title=row['Title'],
                    Author=row['Author'],
                    Year=row['Year'],
                    Publisher=row['Publisher'],
                    Image_URL_L=row['ImageURl'],
                    num_of_rating=row['num_of_rating']
                    )
                    final_rating_obj.save()
        print("Data loaded successfully.")
    except Exception as e:
        print("Error loading data:", str(e))

if __name__ == "__main__":
    load_final_rating_data()
