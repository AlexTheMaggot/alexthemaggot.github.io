from django.db import models


class TabletBrand(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='static/img/tabletbrands/')

    class Meta:

        verbose_name = 'TabletBrand'
        verbose_name_plural = 'TabletBrands'

    def __str__(self):
        return self.name


class TabletModel(models.Model):
    
    brand = models.ForeignKey(TabletBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    img = models.ImageField(upload_to='static/img/tabletmodels')

    class Meta:

        verbose_name = 'TabletModel'
        verbose_name_plural = 'TabletModels'

    def __str__(self):
        return self.name
