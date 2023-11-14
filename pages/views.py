from django.shortcuts import render
from .models import MainContent

# Create your views here.
def main(request):
    return render(request, 'pages/main.html')

def company(request):
    return render(request, 'pages/company.html')

def product(request):
    return render(request, 'pages/product.html')

def mall(request):
    return render(request, 'pages/mall.html')

def sign(request):
    return render(request, 'pages/sign.html')