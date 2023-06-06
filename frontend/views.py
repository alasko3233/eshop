from django.db.models import Count
from django.shortcuts import render
from .models import Category, Product

# Create your views here.


def home(request):
    produits = Product.objects.all()
    categories = Category.objects.annotate(nbre_produits=Count('products'))

    return render(request, "pages/index.html", {'produits': produits, 'categories': categories})


def shop(request):
    return render(request, "pages/shop.html")


def detail(request, id):
    produit = Product.objects.get(id=id)
    produitsC = Product.objects.filter(category_id=produit.category)
    context = {'produit': produit, 'produitsC': produitsC}
    return render(request, "pages/detail.html", context)


def contact(request):
    return render(request, "pages/contact.html")


def cart(request):
    return render(request, "pages/cart.html")


def checkout(request):
    return render(request, "pages/checkout.html")


def categories(request, id):
    produits = Product.objects.filter(category_id=id)
    context = {'produit': produits}

    return render(request, "pages/checkout.html", context)
