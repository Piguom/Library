# Generated by Django 2.0.1 on 2018-01-04 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0032_auto_20180104_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panier',
            name='product',
        ),
    ]
