# Generated by Django 3.2.16 on 2022-12-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_alter_booking_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
