# Generated by Django 2.2 on 2022-06-17 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_tran_dis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='totaldeposit',
            new_name='avaliablebalance',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='accountbalance',
            new_name='checkingbalance',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='totalprofit',
            new_name='curentbalance',
        ),
    ]