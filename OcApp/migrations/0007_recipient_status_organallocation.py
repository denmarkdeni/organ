# Generated by Django 5.0.1 on 2025-01-30 10:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OcApp', '0006_organ_blood_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='status',
            field=models.CharField(default='Waiting', max_length=20),
        ),
        migrations.CreateModel(
            name='OrganAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('reviewed_at', models.DateTimeField(auto_now=True)),
                ('organ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OcApp.organ')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OcApp.recipient')),
                ('reviewed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approvals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
