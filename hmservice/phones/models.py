from django.db import models


class PhoneBrand(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='static/img/phonebrands/')

    class Meta:
        verbose_name = "Бренд телефонов"
        verbose_name_plural = "Бернды телефонов"

    def __str__(self):
        return self.name


class PhoneModel(models.Model):

    brand = models.ForeignKey(PhoneBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    img = models.ImageField(upload_to='static/img/phonemodels/')
    serv1 = models.CharField(max_length=50, default='Диагностика')
    price1 = models.IntegerField(default=0)
    serv2 = models.CharField(max_length=50, default='Замена дисплея')
    price2 = models.IntegerField(default=2000)
    serv3 = models.CharField(max_length=50, default='Замена разъема питания')
    price3 = models.IntegerField(default=1000)
    serv4 = models.CharField(max_length=50, default='Замена аккумулятора')
    price4 = models.IntegerField(default=1000)
    serv5 = models.CharField(max_length=50, default='Замена микрофона')
    price5 = models.IntegerField(default=800)
    serv6 = models.CharField(max_length=50, default='Замена динамика')
    price6 = models.IntegerField(default=700)
    serv7 = models.CharField(max_length=50, default='Замена камеры')
    price7 = models.IntegerField(default=1000)
    serv8 = models.CharField(max_length=50, default='Прошивка аппарата')
    price8 = models.IntegerField(default=1000)
    serv9 = models.CharField(max_length=50, default='Замена платы')
    price9 = models.IntegerField(default=2500)
    serv10 = models.CharField(max_length=50, default='Замена кнопок')
    price10 = models.IntegerField(default=500)

    class Meta:
        verbose_name = "Модель телефонов"
        verbose_name_plural = "Модели телефонов"

    def __str__(self):
        return self.name
    
