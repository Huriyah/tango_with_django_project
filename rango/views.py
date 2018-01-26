from django.shortcuts import render
from rango.models import Category
from django.http import HttpResponse
from rango.models import Page

# Create your views here.

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)

        
        
        
        

def index(request):
    page_list = Page.objects.order_by('-views')[:5]
    category_list = Category.objects.order_by('-likes')[:5]
    context_dic = {'categories': category_list, 'pages': page_list}
    return render(request, 'rango/index.html', context_dic)

def about(request):
    context_dic = {}
    return render(request, 'rango/about.html', context = context_dic)




