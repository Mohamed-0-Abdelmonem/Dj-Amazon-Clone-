# Generated by Django 4.2.4 on 2024-01-29 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_alter_order_code_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='VXX8Y4T0', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Processed', 'Processed'), ('Shipped', 'Shipped'), ('Recieved', 'Recieved')], default='Recieved', max_length=10),
        ),
    ]
