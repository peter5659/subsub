# Generated by Django 2.1.1 on 2020-09-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='edit',
            field=models.IntegerField(default=0),
        ),
    ]
