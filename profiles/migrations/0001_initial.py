# Generated by Django 3.2.15 on 2022-09-23 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('default_address_line1', models.CharField(blank=True, max_length=80, null=True)),
                ('default_address_line2', models.CharField(blank=True, max_length=80, null=True)),
                ('default_eircode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('default_county', models.CharField(blank=True, max_length=80, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
