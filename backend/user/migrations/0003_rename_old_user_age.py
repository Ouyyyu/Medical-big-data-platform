# Generated by Django 4.1 on 2022-08-16 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='old',
            new_name='age',
        ),
    ]
