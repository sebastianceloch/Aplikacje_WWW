# Generated by Django 4.2.7 on 2023-12-02 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_user_home_address_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
