from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'pages/main.html')

def company(request):
    return render(request, 'pages/company.html')

def product(request):
    return render(request, 'pages/product.html')
