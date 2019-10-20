from django.db import models


class CameraBrand(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='static/img/camerabrands/')

    class Meta:
        verbose_name = "CameraBrand"
        verbose_name_plural = "CameraBrands"

    def __str__(self):
        return self.name


class CameraModel(models.Model):

    brand = models.ForeignKey(CameraBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    img = models.ImageField(upload_to='static/img/cameramodels/')

    class Meta:
        verbose_name = "CameraModel"
        verbose_name_plural = "CameraModels"

    def __str__(self):
        return self.name
    
