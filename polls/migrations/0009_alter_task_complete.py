# Generated by Django 4.2.7 on 2023-12-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_task_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
