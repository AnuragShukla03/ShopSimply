# Generated by Django 4.0 on 2021-12-23 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_customer_due'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Due',
            new_name='DueDate',
        ),
    ]
