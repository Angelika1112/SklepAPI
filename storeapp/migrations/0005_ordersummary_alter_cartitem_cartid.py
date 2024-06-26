# Generated by Django 5.0.3 on 2024-05-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0004_alter_cartitem_cartid'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSummary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('itemList', models.CharField(max_length=200)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('firstName', models.CharField(max_length=15)),
                ('lastName', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=25)),
                ('homeNumber', models.CharField(max_length=10)),
                ('zipCode', models.CharField(max_length=6)),
                ('phoneNumber', models.CharField(max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cartId',
            field=models.CharField(max_length=36),
        ),
    ]
