from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from book.models import Final_Rating
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.core.paginator import Paginator

from book.models import Final_Rating

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

def book_details(request, book_id):
    book = get_object_or_404(Final_Rating, pk=book_id)
    return render(request, 'book_details.html', {'book': book})

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
