# Generated by Django 2.2 on 2022-02-18 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_remove_customuser_zipcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='cardnumber',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='cvc',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='id1',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='id2',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='name_oncard',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='postal',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='ssn',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='state',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='street',
        ),
    ]