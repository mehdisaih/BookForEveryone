from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignInForm , SignUpForm
<<<<<<< Updated upstream
from .forms import AddToCartForm
from book.models import Final_Rating
from book.models import Cart, CartItem,Item
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
=======
from book.models import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
>>>>>>> Stashed changes




def index(request):
    return render(request, 'index.html')

def books(request):
    return render(request, 'books.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cart.objects.create(user=user)
            return redirect('/')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
    


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('/')  
            else:
                error_msg = "Invalid username or password."
                return render(request, 'signin.html', {'form': form, 'error_msg': error_msg})
        else:
            error_msg = "Invalid form data."
            return render(request, 'signin.html', {'form': form, 'error_msg': error_msg})
    else:
        form = SignInForm()
        return render(request, 'signin.html', {'form': form})
    
def book_details(request, book_id):
    book = get_object_or_404(Final_Rating, pk=book_id)
    return render(request, 'book_details.html', {'book': book})

@login_required
def view_cart(request):
    # Récupérer le panier de l'utilisateur actuellement connecté
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Récupérer le contenu du panier et le total
    cart_items = cart.cartitem_set.all()
    total_price = ...  # Calculez le total du panier

    # Passer les données au template cart.html
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, book_id):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            # Print the retrieved book_id for debugging
            print(f"Retrieved book_id from form: {book_id}")

            # Retrieve the article to add to the cart
            book = get_object_or_404(Final_Rating, ISBN=book_id)

            # ... rest of your code for adding the book to the cart ...

    else:
        form = AddToCartForm()

    return render(request, 'book_details.html', {'form': form})

<<<<<<< Updated upstream
 
=======
    
    
@login_required
def default(request):
    profile = User.objects.get(user=request.user)    
    return render(request, 'profile.html', {'profile': profile})

def logout(request):
    django_logout(request)
    return redirect('signin')
>>>>>>> Stashed changes
