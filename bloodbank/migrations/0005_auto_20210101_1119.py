# Generated by Django 3.1.3 on 2021-01-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0004_auto_20210101_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='AssocHB',
            field=models.CharField(default='--', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donor',
            name='ReferenceID',
            field=models.CharField(default='--', max_length=100),
            preserve_default=False,
        ),
    ]