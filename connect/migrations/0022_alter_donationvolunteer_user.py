# Generated by Django 5.1.4 on 2025-01-31 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0021_donationvolunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationvolunteer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='connect.volunteerdetails'),
        ),
    ]
