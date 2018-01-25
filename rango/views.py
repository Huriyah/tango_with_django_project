from django.shortcuts import render
from rango.models import Category
from django.http import HttpResponse

# Create your views here.


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dic = {'categories': category_list}
    return render(request, 'rango/index.html', context_dic)

def about(request):
    context_dic = {}
    return render(request, 'rango/about.html', context = context_dic)




