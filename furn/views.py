from django.shortcuts import render, redirect
from django.views import generic
from furn.models import *
from furn.form import *

def home(request):

    category = request.GET.get('category')
    if category == None:
        arrivals = Arrival.objects.all()
    else:
        arrivals = Arrival.objects.filter(category__category_name=category)

    blog = Blog.objects.all()
    base = Carousel.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'pages/home.html', {
        "base": base,
         "blog":blog,
         "arrivals":arrivals,
         "products":products,
         "categories":categories,
        })
    
def arrivals_detail(request, pk):
    
    arrivals_details = Arrival.objects.get(id=pk)
    
    context = {
        "arrivals_details": arrivals_details,
    }
    return render(request, 'details/arrival_detail.html', context)

def signup(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = Registration()
        
    return render(request, 'registration/signup.html', {"form":form})

def logout_redirect(request):
    return render(request, 'registration/logout-redirect.html')

