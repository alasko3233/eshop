from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path("details/<int:id>/", views.detail, name='detail'),
    path('shop', views.shop, name='shop'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path("categories/<int:id>", views.categories, name='categories'),


]
