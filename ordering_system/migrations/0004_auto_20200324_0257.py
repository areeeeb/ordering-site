# Generated by Django 3.0.4 on 2020-03-23 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering_system', '0003_auto_20200324_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='speciality',
            field=models.BooleanField(default=False),
        ),
    ]