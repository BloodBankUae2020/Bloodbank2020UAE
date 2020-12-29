# Generated by Django 3.1.3 on 2020-12-29 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('emailid', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=300)),
                ('mdate', models.DateField()),
                ('isread', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgroup', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HospitalName', models.CharField(max_length=100)),
                ('ContactNo', models.CharField(max_length=15)),
                ('Location', models.CharField(max_length=300, null=True)),
                ('Aplus', models.CharField(max_length=10)),
                ('Aminus', models.CharField(max_length=10)),
                ('Bplus', models.CharField(max_length=10)),
                ('Bminus', models.CharField(max_length=10)),
                ('ABplus', models.CharField(max_length=10)),
                ('ABminus', models.CharField(max_length=10)),
                ('Oplus', models.CharField(max_length=10)),
                ('Ominus', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Context', models.CharField(max_length=300)),
                ('Subject', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('mobileno', models.CharField(max_length=15)),
                ('emailid', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=15)),
                ('age', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=300, null=True)),
                ('message', models.CharField(max_length=300, null=True)),
                ('postingdate', models.DateField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbank.group')),
            ],
        ),
    ]
