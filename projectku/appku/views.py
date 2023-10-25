from django.shortcuts import render



def index(request):
    return render(request, 'appku/index.html')

def home(request):
    return render(request, 'appku/home.html')