# Generated by Django 2.2.4 on 2020-01-02 23:33

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0068_auto_20191211_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('title', models.TextField(blank=True, default='')),
                ('desc', models.TextField(blank=True, default='')),
                ('url', models.URLField(db_index=True)),
                ('valid_from', models.DateTimeField(db_index=True)),
                ('valid_to', models.DateTimeField(db_index=True)),
                ('key', models.CharField(db_index=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OfferAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('what', models.CharField(db_index=True, max_length=50)),
                ('offer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='townsquare.Offer')),
                ('profile', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='offeractions', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('activity', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='dashboard.Activity')),
                ('profile', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('comment', models.TextField(blank=True, default='')),
                ('activity', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='dashboard.Activity')),
                ('profile', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
