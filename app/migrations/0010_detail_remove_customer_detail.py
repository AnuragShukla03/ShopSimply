# Generated by Django 4.0 on 2021-12-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_customer_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=50)),
                ('Contact', models.BigIntegerField()),
                ('Date', models.TextField(max_length=50)),
                ('Detail', models.TextField(default=' ', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Detail',
        ),
    ]
