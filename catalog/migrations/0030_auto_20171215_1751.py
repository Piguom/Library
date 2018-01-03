# Generated by Django 2.0 on 2017-12-15 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0029_auto_20171215_1514'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='field',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='field',
            name='model',
        ),
        migrations.AlterUniqueTogether(
            name='model',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='model',
            name='app',
        ),
        migrations.AlterUniqueTogether(
            name='setting',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='setting',
            name='field',
        ),
        migrations.DeleteModel(
            name='App',
        ),
        migrations.DeleteModel(
            name='Field',
        ),
        migrations.DeleteModel(
            name='Model',
        ),
        migrations.DeleteModel(
            name='Setting',
        ),
    ]
