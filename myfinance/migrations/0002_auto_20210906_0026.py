# Generated by Django 3.2.7 on 2021-09-05 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 6, 0, 26, 22, 976154)),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]