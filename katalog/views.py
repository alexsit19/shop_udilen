from django.shortcuts import render
from .models import Categories, Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    categories = Categories.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'base.html', context)

def categories(request, alias):
    categories = Categories.objects.all()
    for cat in categories:
        if cat.alias == alias:
            cat_id = cat.id
            break

    products_list = Products.objects.filter(category=cat_id)
    paginator = Paginator(products_list, 6) #показывать 6 продуктов на странице
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # если страница не целое число, возвращаем первую страницу
        products = paginator.page(1)
    except EmptyPage:
        # если номер страницы выходит за пределы выдаем последнюю страницу
        products = paginator.page(paginator.num_pages)
    """for cat in categories:
        if cat.alias == alias:
            category = cat.name
            break

    products = Products.objects.filter(category=category)"""
    context = {
        'categories': categories,
        #'name': cat_name,
        'products': products,
    }


    return render(request, 'categories.html', context)
