# Generated by Django 2.2 on 2022-06-07 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220607_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdraw',
            old_name='banknmae',
            new_name='bankname',
        ),
    ]
