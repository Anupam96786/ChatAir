# Generated by Django 3.1.5 on 2021-01-15 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20210116_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercontact',
            name='contacts',
        ),
    ]
