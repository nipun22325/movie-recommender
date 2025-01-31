# Generated by Django 5.0.6 on 2024-07-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('movie_description', models.TextField()),
                ('movie_image', models.ImageField(upload_to='photos/')),
                ('age_limit', models.IntegerField()),
                ('genre', models.ManyToManyField(to='add.genre')),
            ],
        ),
    ]
