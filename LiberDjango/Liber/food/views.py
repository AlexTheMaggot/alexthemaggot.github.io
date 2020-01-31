from django.shortcuts import render, get_object_or_404
from .models import Tag, Restaurant, DishCategory, Dish


def restaurant_list(request):
    tag = Tag.objects.all()
    restaurant = Restaurant.objects.all()
    context = {
        'tag': tag,
        'restaurant': restaurant,
    }
    return render(request, 'food/restaurant_list.html', context)

def dish_list(request, slug):
    restaurant = get_object_or_404(Restaurant, slug__iexact=slug)
    context = {
        'restaurant': restaurant,
    }
    return render(request, 'food/dish_list.html', context)