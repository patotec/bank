# Generated by Django 2.2 on 2022-02-14 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20220214_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='zipcode',
        ),
    ]