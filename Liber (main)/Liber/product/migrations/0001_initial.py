# Generated by Django 3.0.2 on 2020-01-21 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название категории: ')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категория блюд',
                'verbose_name_plural': 'Категории блюд',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название тега: ')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название ресторана: ')),
                ('slug', models.SlugField(unique=True)),
                ('img', models.ImageField(upload_to='static/img/food/restaurants/', verbose_name='Изображение: ')),
                ('description', models.TextField(verbose_name='Описание: ')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Рейтинг: ')),
                ('time_delivery', models.IntegerField(max_length=2, verbose_name='Время доставки: ')),
                ('tags', models.ManyToManyField(related_name='tag', to='product.Tag', verbose_name='Теги: ')),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Рестораны',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название блюда: ')),
                ('slug', models.SlugField(unique=True)),
                ('img', models.ImageField(upload_to='static/img/food/dishes/', verbose_name='Изображение: ')),
                ('description', models.TextField(verbose_name='Описание: ')),
                ('available', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='product.DishCategory', verbose_name='Категория блюда')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='restaurant', to='product.Restaurant', verbose_name='Ресторан: ')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
    ]
