# Generated by Django 4.0 on 2021-12-23 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_due_customer_duedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='DueDate',
        ),
    ]
