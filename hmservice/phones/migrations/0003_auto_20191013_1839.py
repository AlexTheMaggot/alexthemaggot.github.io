# Generated by Django 2.2.4 on 2019-10-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phonemodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='slug',
            field=models.SlugField(),
        ),
    ]
