# Generated by Django 3.0.4 on 2020-03-23 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordering_system', '0002_pizza_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='large_p',
            new_name='large_price',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='regular_p',
            new_name='regular_price',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='small_p',
            new_name='small_price',
        ),
    ]