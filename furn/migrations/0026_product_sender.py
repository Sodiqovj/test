# Generated by Django 4.1 on 2022-09-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0025_alter_product_rate_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sender',
            field=models.CharField(default='user', max_length=100),
        ),
    ]
