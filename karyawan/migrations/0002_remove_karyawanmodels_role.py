# Generated by Django 4.1.1 on 2022-12-14 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='karyawanmodels',
            name='role',
        ),
    ]
