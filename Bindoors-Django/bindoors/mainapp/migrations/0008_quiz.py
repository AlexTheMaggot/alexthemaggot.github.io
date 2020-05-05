# Generated by Django 3.0.1 on 2020-05-04 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_sendcatandprice_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_type', models.CharField(max_length=200, verbose_name='Тип двери')),
                ('price_type', models.CharField(max_length=200, verbose_name='Ценовой сегмент')),
                ('style_type', models.CharField(max_length=200, verbose_name='Стиль')),
                ('size_type', models.CharField(max_length=200, verbose_name='Размер')),
                ('material_type', models.CharField(max_length=200, verbose_name='Материал')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone', models.CharField(max_length=200, verbose_name='Телефон')),
                ('mail', models.CharField(max_length=200, verbose_name='Почта')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заявка с квиза',
                'verbose_name_plural': 'Заявки с квиза',
            },
        ),
    ]