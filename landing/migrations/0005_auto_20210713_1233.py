# Generated by Django 2.2.18 on 2021-07-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20210708_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infopage',
            options={'verbose_name': 'Цена и телефон', 'verbose_name_plural': 'Цены и телефоны'},
        ),
        migrations.AddField(
            model_name='order',
            name='order_quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]