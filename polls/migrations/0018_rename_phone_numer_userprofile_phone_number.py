# Generated by Django 4.2.7 on 2023-11-22 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_remove_userprofile_avatar_userprofile_home_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone_numer',
            new_name='phone_number',
        ),
    ]
