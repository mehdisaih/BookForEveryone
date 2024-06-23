import json
import re
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from book.models import Cart, Final_Rating, cartitems
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.core.paginator import Paginator
import pickle
from book.models import Final_Rating
import numpy as np
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import requests
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Cart, cartitems



model=pickle.load(open('C:\\Users\\dell\\Desktop\\BookForEveryone\\Model\\artifacts\\model.pkl','rb'))
book_pivot=pickle.load(open('C:\\Users\\dell\\Desktop\\BookForEveryone\\Model\\artifacts\\book_pivot.pkl','rb'))

def index(request):
    query = request.GET.get('q')
    if query:
        random_books = Final_Rating.objects.filter(
            Q(Title__icontains=query) | Q(Author__icontains=query)
        ).order_by('?')[:60]

    else:
        random_books = Final_Rating.objects.filter(Rating__gte=7).order_by('?')[:8]


    paginator = Paginator(random_books, 20)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books.html', {'page_obj': page_obj})

def clean_title(title):
    return re.sub(r'\W+', '', title.lower())

def book_details(request, book_id):
    book = get_object_or_404(Final_Rating, pk=book_id)
    book_id = np.where(book_pivot.index == book.Title)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=4)

    suggested_books = []
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for book_title in books:
            if clean_title(book_title) == clean_title(book.Title):
                suggested_books.extend(Final_Rating.objects.filter(Title__iexact=book_title))

    print(suggestion,books,suggested_books)
    return render(request, 'book_details.html', {'book': book, 'suggested_books': suggested_books})

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
<<<<<<< Updated upstream
 
def book_details(request, book_id):
    book = get_object_or_404(Final_Rating, pk=book_id)
    return render(request, 'book_details.html', {'book': book})

=======


def addtocart(req):
    data=json.loads(req.body)
    product_id = data["id"]
    product=Final_Rating.objects.get(id=product_id)
    if req.user.is_authenticated:
        cart, created=Cart.objects.get_or_create(user=req.user,complete=False)
        cartitem, created=cartitems.objects.get_or_create(cart=cart,Final_Rating=product)
        cartitem.quantity +=1
        cartitem.save()

        print(cartitem)
    return JsonResponse("it is working",safe=False)

def cart(request):
    
    cart = None
    cartitems = []
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, complete=False)
        cartitems = cart.cartitem.all()
    
    context = {"cart":cart , "cartitems":cartitems}
    return render(request, "cart.html", context)

def removefromcart(request, id):
    cart_item = get_object_or_404(cartitems, id=id)
    cart_item.delete()
    return redirect('cart')

def addquantity(request, id, quantity):
    cart_item = get_object_or_404(cartitems, id=id)
    cart_item.quantity = int(quantity)
    cart_item.save()
    return redirect('cart')

def removequantity(request, id,quantity):
    cart_item = get_object_or_404(cartitems, id=id)
    cart_item.quantity = int(quantity)
    cart_item.save()
    return redirect('cart')

def make_purchase(request):
    filename = f"receipt-{request.user.username}.pdf"
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    p = canvas.Canvas(response)
    cart, created = Cart.objects.get_or_create(user=request.user, complete=False)
    cartitems = cart.cartitem.all()
    y_position = 800
    p.drawString(100, y_position, "Reçu d'achat")
    total_price = 0
    for item in cartitems:
        y_position -= 20
        line = f"{item.Final_Rating.Title}: {item.quantity} x {item.Final_Rating.num_of_rating}"
        p.drawString(100, y_position, line)
        total_price += item.Final_Rating.num_of_rating * item.quantity

    y_position -= 40
    p.drawString(100, y_position, f"Total: {total_price}")

    p.showPage()
    p.save()
    cartitems.delete()

    return response
>>>>>>> Stashed changes
