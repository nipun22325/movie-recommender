# Generated by Django 5.0.6 on 2024-07-07 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='age_limit',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='genre',
            new_name='genres',
        ),
    ]
