# Generated by Django 3.1.3 on 2021-01-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0006_auto_20210101_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='donation_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
    ]
