# Generated by Django 4.2.16 on 2024-10-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_food_name_food_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False),
        ),
    ]
