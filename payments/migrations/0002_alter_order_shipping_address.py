# Generated by Django 5.0.3 on 2024-03-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(max_length=15500),
        ),
    ]
