# Generated by Django 5.0.7 on 2024-07-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='max_capacity',
            field=models.IntegerField(default=100),
        ),
    ]
