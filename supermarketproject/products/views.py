from .models import products
from django.shortcuts import render
from django.shortcuts import get_object_or_404 
from django.shortcuts import redirect
def home(request):
    return render(request, 'home.html')

def addproduct(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        products.objects.create(product_name=product_name, category=category, price=price, quantity=quantity)
    return render(request, 'add_products.html')

def viewproducts(request):
    p = products.objects.all()
    return render(request, 'view_products.html', {'products': p})

def dproduct(request, id):
    product = get_object_or_404(products, id=id)
    product.delete()
    return redirect('viewproducts')

def editproduct(request, id):
    product = get_object_or_404(products, id=id)
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.category = request.POST.get('category')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.save()
        return redirect('viewproducts')
    return render(request, 'edit_product.html', {'p': product})
