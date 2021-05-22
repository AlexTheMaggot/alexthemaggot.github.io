from django.db import models


class TabletBrand(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='static/img/tabletbrands/')

    class Meta:

        verbose_name = 'Бренд планшетов'
        verbose_name_plural = 'Бренды планшетов'

    def __str__(self):
        return self.name


class TabletModel(models.Model):
    
    brand = models.ForeignKey(TabletBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    img = models.ImageField(upload_to='static/img/tabletmodels')
    serv1 = models.CharField(max_length=50, default='Замена Дисплея')
    price1 = models.IntegerField(default=1000)
    serv2 = models.CharField(max_length=50, default='Замена Дисплея')
    price2 = models.IntegerField(default=1000)
    serv3 = models.CharField(max_length=50, default='Замена Дисплея')
    price3 = models.IntegerField(default=1000)
    serv4 = models.CharField(max_length=50, default='Замена Дисплея')
    price4 = models.IntegerField(default=1000)
    serv5 = models.CharField(max_length=50, default='Замена Дисплея')
    price5 = models.IntegerField(default=1000)
    serv6 = models.CharField(max_length=50, default='Замена Дисплея')
    price6 = models.IntegerField(default=1000)
    serv7 = models.CharField(max_length=50, default='Замена Дисплея')
    price7 = models.IntegerField(default=1000)
    serv8 = models.CharField(max_length=50, default='Замена Дисплея')
    price8 = models.IntegerField(default=1000)
    serv9 = models.CharField(max_length=50, default='Замена Дисплея')
    price9 = models.IntegerField(default=1000)
    serv10 = models.CharField(max_length=50, default='Замена Дисплея')
    price10 = models.IntegerField(default=1000)

    class Meta:

        verbose_name = 'Модель планшетов'
        verbose_name_plural = 'Модели планшетов'

    def __str__(self):
        return self.name