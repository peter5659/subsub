# Generated by Django 2.1.1 on 2020-09-20 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200912_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
