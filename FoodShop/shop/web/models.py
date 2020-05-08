from django.db import models
from PIL import Image


class Product(models.Model):
    FRUIT = 'fruit'
    SEA = 'sea'
    DAIRY = 'dairy'
    BEVERAGES = 'beverages'

    CHOICE_GROUP = {
        (FRUIT, 'fruit'),
        (SEA, 'sea'),
        (DAIRY, 'dairy'),
        (BEVERAGES, 'beverages'),
    }
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField()
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=FRUIT)
    img = models.ImageField(default='noimage.jpg', upload_to='product_image')

    def __str__(self):
        return  f'{self.name}'