# Generated by Django 2.2 on 2022-06-07 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_otp_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pay_method',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='price',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='wallet',
        ),
    ]
