from django.shortcuts import render
from .models import MainContent

# Create your views here.
def main(request):
    return render(request, 'pages/main.html')

def company(request):
    return render(request, 'pages/company.html')

def product(request):
    return render(request, 'pages/product.html')

def buying(request):
    return render(request, 'pages/buying.html')