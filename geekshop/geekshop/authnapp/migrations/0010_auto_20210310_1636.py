# Generated by Django 2.2.17 on 2021-03-10 16:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0009_auto_20210310_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 12, 16, 36, 14, 729605, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
