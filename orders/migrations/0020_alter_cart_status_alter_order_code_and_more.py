# Generated by Django 4.2.4 on 2024-03-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_alter_cart_status_alter_order_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('InProgress', 'InProgress')], max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='2BIR2N8T', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Recieved', 'Recieved'), ('Processed', 'Processed'), ('Shipped', 'Shipped')], default='Recieved', max_length=10),
        ),
    ]