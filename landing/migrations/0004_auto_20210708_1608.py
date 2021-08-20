# Generated by Django 2.2.18 on 2021-07-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20210628_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_page', models.IntegerField(verbose_name='Цена 1 схемы')),
                ('phone_page', models.CharField(max_length=20, verbose_name='Телефон')),
            ],
        ),
        migrations.AlterField(
            model_name='statusorder',
            name='status_name',
            field=models.CharField(max_length=200, verbose_name='Название статуса'),
        ),
    ]