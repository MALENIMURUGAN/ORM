# Generated by Django 4.2.5 on 2023-10-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Football',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('score', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
            ],
        ),
    ]
