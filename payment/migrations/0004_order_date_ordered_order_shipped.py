# Generated by Django 5.1.1 on 2024-11-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_remove_order_date_ordered_remove_order_shipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]
