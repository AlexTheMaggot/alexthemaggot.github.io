# Generated by Django 2.2.4 on 2019-10-20 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CameraBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('logo', models.ImageField(upload_to='static/img/camerabrands/')),
            ],
            options={
                'verbose_name': 'CameraBrand',
                'verbose_name_plural': 'CameraBrands',
            },
        ),
        migrations.CreateModel(
            name='CameraModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('img', models.ImageField(upload_to='static/img/cameramodels/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cameras.CameraBrand')),
            ],
            options={
                'verbose_name': 'CameraModel',
                'verbose_name_plural': 'CameraModels',
            },
        ),
    ]