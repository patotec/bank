# Generated by Django 2.2 on 2022-03-11 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_customuser_is_email_verified'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Join_Plan',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='gift',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='maxdeposit',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='maxreturn',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='mindeposit',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='minreturn',
        ),
        migrations.DeleteModel(
            name='Profit',
        ),
    ]
