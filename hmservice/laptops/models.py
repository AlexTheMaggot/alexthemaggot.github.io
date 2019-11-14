from django.db import models


class LaptopBrand(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='static/img/laptopbrands/')

    class Meta:

        verbose_name = 'Бренд ноутбуков'
        verbose_name_plural = 'Бренды ноутбуков'

    def __str__(self):
        return self.name


class LaptopModel(models.Model):

    brand = models.ForeignKey(LaptopBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    img = models.ImageField(upload_to='static/img/laptopmodels/')

    class Meta:

        verbose_name = 'Модель ноутбуков'
        verbose_name_plural = 'Модели ноутбуков'

    def __str__(self):
        return self.name
