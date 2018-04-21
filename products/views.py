#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.contrib.auth.decorators import login_required
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from products.models import Product
from products.serializers import ProductSerializer

@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                'products/product/list.html',
                {'category': category,
                'categories': categories,
                'products': products})
@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                    'products/product/detail.html',
                    {'product': product,
                    'cart_product_form': cart_product_form})
def product_list_all(request):
    """
    List all code products, or create a product.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def delete(request, id):
    try:
        product = Product.objects.get(pk=id)
        product.delete()
        return HttpResponse('deleted')
    except Product.DoesNotExist:
        return HttpResponse(status=404)    

