# Generated by Django 5.0 on 2023-12-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_alter_portfoliofinancialinstrument_buy_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialinstrumentapidata',
            name='actual_price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]