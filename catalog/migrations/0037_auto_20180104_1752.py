# Generated by Django 2.0.1 on 2018-01-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0036_auto_20180104_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panieritem',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=5),
        ),
    ]
