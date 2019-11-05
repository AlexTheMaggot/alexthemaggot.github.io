# Generated by Django 2.2.4 on 2019-11-03 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainFeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'MainFeedback',
                'verbose_name_plural': 'MainFeedbacks',
            },
        ),
    ]
