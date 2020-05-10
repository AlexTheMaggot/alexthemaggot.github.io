import telebot

from django.shortcuts import render, redirect
from .models import Product
from .forms import OrderForm
from django.views import View

bot = telebot.TeleBot('1051471905:AAEf8-enWvdUxNtCAHuUcb0QmNBaWa0am98')


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


class OrderView(View):
    def post(self, request):
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data['name']
                price = form.cleaned_data['price']
                message = 'Новый заказ с магазина!' + '\r\n' + '\r\n' + 'Товар: ' + name + '\r\n' + 'Цена: ' + price
                bot.send_message(104566710, message)
                return redirect('/shop')
        return redirect('/shop')
