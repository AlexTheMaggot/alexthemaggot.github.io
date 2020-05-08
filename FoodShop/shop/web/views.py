from django.shortcuts import render
from web.models import Product
from django.views.generic.base import View


def index(request):
    return render(request, 'web/index.html')


def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'web/shop.html', context)


def ShopDetailView(View):
    """Полное описание проекта"""
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, "web/product_detail.html", {"product": product})
