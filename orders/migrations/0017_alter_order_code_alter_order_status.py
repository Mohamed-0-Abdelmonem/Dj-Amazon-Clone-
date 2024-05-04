# Generated by Django 4.2.4 on 2024-03-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_alter_order_code_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='NV5D8N0C', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Recieved', 'Recieved'), ('Processed', 'Processed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Recieved', max_length=10),
        ),
    ]