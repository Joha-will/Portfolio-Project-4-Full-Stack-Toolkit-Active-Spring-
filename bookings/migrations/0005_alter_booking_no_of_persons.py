# Generated by Django 3.2.16 on 2022-12-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20221213_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_persons',
            field=models.IntegerField(help_text='How many to swim?'),
        ),
    ]
