from django.db import models


class CameraBrand(models.Model):

    name = models.CharField('Название бренда', max_length=50)
    slug = models.SlugField('Слаг-поле (То же, что и название бренда, только вместо пробела тире)')
    logo = models.ImageField('Изображение (формат PNG размер 200x200)', upload_to='static/img/camerabrands/')

    class Meta:
        verbose_name = "Бренд Фотоаппаратов"
        verbose_name_plural = "Бренды Фотоаппаратов"

    def __str__(self):
        return self.name


class CameraModel(models.Model):

    brand = models.ForeignKey(CameraBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    img = models.ImageField(upload_to='static/img/cameramodels/')

    class Meta:
        verbose_name = "Модель Фотоаппаратов"
        verbose_name_plural = "Модели Фотоаппаратов"

    def __str__(self):
        return self.name
    
