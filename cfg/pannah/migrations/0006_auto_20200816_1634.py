# Generated by Django 3.1 on 2020-08-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pannah', '0005_merge_20200816_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheme',
            name='customer',
        ),
        migrations.AddField(
            model_name='scheme',
            name='customer',
            field=models.ManyToManyField(to='pannah.Customer'),
        ),
    ]
