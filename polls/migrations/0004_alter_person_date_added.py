# Generated by Django 4.2.6 on 2023-11-06 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_job_alter_person_options_remove_person_shirt_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_added',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
