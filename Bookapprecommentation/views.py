from django.shortcuts import render




def index(request):
    return render(request, 'index.html')

def books(request):
    return render(request, 'books.html')

def about(request):
    return render(request, 'about.html')
 