# Generated by Django 2.2.4 on 2019-11-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_auto_20191028_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='price1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='price10',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='price2',
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='price5',
            field=models.IntegerField(default=800),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='price6',
            field=models.IntegerField(default=700),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='price9',
            field=models.IntegerField(default=2500),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='serv1',
            field=models.CharField(default='Диагностика', max_length=50),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='serv10',
            field=models.CharField(default='Замена кнопок', max_length=50),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='serv2',
            field=models.CharField(default='Замена дисплея', max_length=50),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='serv3',
            field=models.CharField(default='Замена разъема питания', max_length=50),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='serv4',
            field=models.CharField(default='Замена аккумулятора', max_length=50),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='serv5',
            field=models.CharField(default='Замена микрофона', max_length=50),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='serv6',
            field=models.CharField(default='Замена динамика', max_length=50),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='serv7',
            field=models.CharField(default='Замена камеры', max_length=50),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='serv8',
            field=models.CharField(default='Прошивка аппарата', max_length=50),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='serv9',
            field=models.CharField(default='Замена платы', max_length=50),
        ),
    ]
