# Generated by Django 2.0 on 2017-12-14 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_boutique'),
    ]

    operations = [
        migrations.AddField(
            model_name='boutique',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Book'),
        ),
    ]
