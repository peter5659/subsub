# Generated by Django 2.1.1 on 2020-10-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sublist', '0002_auto_20201011_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]