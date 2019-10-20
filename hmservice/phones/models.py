from django.db import models


class PhoneBrand(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='static/img/phonebrands/')

    class Meta:
        verbose_name = "PhoneBrand"
        verbose_name_plural = "PhoneBrands"

    def __str__(self):
        return self.name


class PhoneModel(models.Model):

    brand = models.ForeignKey(PhoneBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    img = models.ImageField(upload_to='static/img/phonemodels/')

    class Meta:
        verbose_name = "PhoneModel"
        verbose_name_plural = "PhoneModels"

    def __str__(self):
        return self.name
    
