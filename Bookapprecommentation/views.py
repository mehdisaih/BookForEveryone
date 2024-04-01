from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignInForm , SignUpForm





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
            form.save()
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

    
    
 