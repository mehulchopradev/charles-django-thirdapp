# Generated by Django 2.1.1 on 2018-10-26 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersroles',
            old_name='role_id',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='usersroles',
            old_name='user_id',
            new_name='user',
        ),
    ]
