from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product
from .forms import ProductSearchForm

def home(request):
    return render(request, 'shop/product_list.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(in_stock=True)

    # Category filter
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Search & price filter
    form = ProductSearchForm(request.GET or None)
    if form.is_valid():
      q = form.cleaned_data.get('q')  
      if q:      
        products = products.filter(name__icontains=q) | products.filter(description__icontains=q)

        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if min_price is not None:
            products = products.filter(price__gte=min_price)
        if max_price is not None:
            products = products.filter(price__lte=max_price)

    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/product_list.html', {
        'category': category,
        'categories': categories,
        'products': page_obj,
        'form': form,
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})
