# Generated by Django 4.0.3 on 2022-04-24 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mmr', models.IntegerField()),
                ('teamHouseX', models.FloatField()),
                ('teamHouseY', models.FloatField()),
                ('sport', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isCapt', models.BooleanField()),
                ('locationX', models.FloatField()),
                ('locationY', models.FloatField()),
                ('teamName', models.TextField()),
            ],
        ),
    ]
