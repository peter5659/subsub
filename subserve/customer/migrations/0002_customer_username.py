# Generated by Django 3.1.1 on 2020-09-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
