# Generated by Django 5.0.1 on 2025-01-28 09:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('userRole', models.CharField(choices=[('doctor', 'Doctor'), ('donor', 'Donor'), ('recipient', 'Recipient'), ('facility', 'Facility'), ('admin', 'Admin')], default='not specified', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
