# Generated by Django 4.0 on 2021-12-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_detail_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Detail',
        ),
        migrations.AddField(
            model_name='customer',
            name='Detail',
            field=models.TextField(default=' ', max_length=50),
        ),
    ]
