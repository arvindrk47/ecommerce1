from django.shortcuts import render, HttpResponse

# Create your views here.
def cart(request):
    return render(request, 'store/cart.html')
