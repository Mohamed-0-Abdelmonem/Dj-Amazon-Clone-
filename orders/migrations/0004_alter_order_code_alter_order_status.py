# Generated by Django 4.2.4 on 2024-02-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='BTL59GPT', max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Processed', 'Processed'), ('Delivered', 'Delivered'), ('Recieved', 'Recieved'), ('Shipped', 'Shipped')], default='Recieved', max_length=10),
        ),
    ]