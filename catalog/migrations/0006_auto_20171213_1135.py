# Generated by Django 2.0 on 2017-12-13 10:35

import catalog.models
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20171213_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url='/images//images/', location='C:\\wamp64\\www\\library\\media/images/'), upload_to=catalog.models.image_directory_path),
        ),
    ]
