# Generated by Django 5.0.3 on 2024-05-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_alter_category_id_alter_item_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartId', models.UUIDField()),
                ('itemId', models.IntegerField(default=0)),
            ],
        ),
    ]
