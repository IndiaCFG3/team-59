# Generated by Django 3.1 on 2020-08-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pannah', '0006_auto_20200816_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='password2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
