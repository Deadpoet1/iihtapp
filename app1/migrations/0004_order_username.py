# Generated by Django 5.1.1 on 2024-09-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_product_out_of_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]