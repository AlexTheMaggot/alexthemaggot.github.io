from django.contrib import admin

from .models import Tag, Restaurant, DishCategory, Dish


class TagConfig(admin.ModelAdmin):
    fields = ('name', 'img', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag, TagConfig)


class RestaurantConfig(admin.ModelAdmin):
    fields = ('name', 'description', 'img', ('rating', 'time_delivery'), 'tags', 'slug')
    list_display = ('name', 'description', 'rating', 'time_delivery')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Restaurant, RestaurantConfig)


class DishCategoryConfig(admin.ModelAdmin):
    fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(DishCategory, DishCategoryConfig)


class DishConfig(admin.ModelAdmin):
    fields = (('name', 'available'), ('restaurant', 'category'), 'description', ('img', 'price'), 'slug')
    list_display = ('name', 'restaurant', 'category', 'price', 'available')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Dish, DishConfig)
