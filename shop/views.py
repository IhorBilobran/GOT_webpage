from django.shortcuts import render, redirect, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Product

def view_categories(request):
	categories = Category.objects.all()
	args = {'categories': categories}
	return render(request, 'shop/categories.html', args)

def view_products(request):
	products = Product.objects.all()
	cart_product_form = CartAddProductForm()
	args = {'products': products, 'cart_product_form': cart_product_form}
	return render(request, 'shop/all_products.html', args)

def view_category(request, id):
	category = get_object_or_404(Category, id=id)
	products = Product.objects.filter(category__id=id)
	args = {'category': category, 'products': products}
	return render(request, 'shop/view_category.html', args)
