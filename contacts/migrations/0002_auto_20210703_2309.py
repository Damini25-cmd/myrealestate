# Generated by Django 3.0.6 on 2021-07-03 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 3, 23, 9, 20, 211356)),
        ),
    ]
