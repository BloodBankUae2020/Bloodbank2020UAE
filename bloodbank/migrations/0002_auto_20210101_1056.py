# Generated by Django 3.1.3 on 2021-01-01 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='AssocHB',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='ReferenceID',
        ),
    ]