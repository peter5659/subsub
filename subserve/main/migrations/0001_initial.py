# Generated by Django 2.1.1 on 2020-09-12 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=45)),
                ('alarm_sms', models.BooleanField()),
                ('alarm_push', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('photo', models.CharField(max_length=45, null=True)),
                ('allergic', models.CharField(max_length=45)),
                ('subscribers', models.IntegerField()),
                ('cycle', models.IntegerField()),
                ('count', models.IntegerField()),
                ('last_subscribers', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('in_event', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('article_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('editted_date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('watched', models.IntegerField()),
                ('locality', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QnA',
            fields=[
                ('article_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('editted_date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('watched', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('review_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('photo', models.CharField(max_length=45, null=True)),
                ('rank', models.IntegerField()),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('longitude', models.DecimalField(decimal_places=20, max_digits=30)),
                ('latitude', models.DecimalField(decimal_places=20, max_digits=30)),
                ('address', models.CharField(max_length=45)),
                ('photo', models.ImageField(upload_to=None)),
                ('subscribers', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('is_premium', models.BooleanField()),
                ('description', models.CharField(max_length=45, null=True)),
                ('sns1', models.CharField(max_length=45, null=True)),
                ('sns2', models.CharField(max_length=45, null=True)),
                ('phone', models.CharField(max_length=45)),
                ('running_time', models.CharField(max_length=45)),
                ('break_time', models.CharField(max_length=45)),
                ('closed_on', models.CharField(max_length=15)),
                ('num_menu', models.IntegerField()),
                ('locality', models.IntegerField()),
                ('comment', models.CharField(max_length=45)),
                ('category', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscribes',
            fields=[
                ('purchased', models.DateTimeField(auto_created=True)),
                ('last_used', models.DateTimeField(auto_created=True)),
                ('end_date', models.DateTimeField(auto_created=True)),
                ('start_date', models.DateTimeField(auto_created=True)),
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('cycle', models.IntegerField()),
                ('remain', models.IntegerField()),
                ('purchased_type', models.IntegerField()),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Menu')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Store')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=45, null=True)),
                ('marketing_email', models.BooleanField()),
                ('marketing_sms', models.BooleanField()),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('barcode', models.IntegerField()),
                ('pusrchasing_type', models.IntegerField(null=True)),
                ('auto_extension', models.BooleanField()),
                ('loaclity', models.IntegerField()),
                ('recent_search_keywords', models.CharField(max_length=45, null=True)),
                ('recent_viewed', models.CharField(max_length=45, null=True)),
                ('profile', models.CharField(max_length=45)),
                ('birthday', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('sex', models.BooleanField()),
                ('certified', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Menu')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Store')),
            ],
        ),
        migrations.AddField(
            model_name='subscribes',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Store'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AddField(
            model_name='menu',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Store'),
        ),
        migrations.AddField(
            model_name='manager',
            name='id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]