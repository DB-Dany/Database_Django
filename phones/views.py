from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    # Получаем параметр сортировки из GET-запроса
    sort = request.GET.get('sort', 'name')

    # Определяем порядок сортировки
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # Получаем телефон по slug или возвращаем 404
    phone = get_object_or_404(Phone, slug=slug)

    context = {
        'phone': phone
    }
    return render(request, template, context)