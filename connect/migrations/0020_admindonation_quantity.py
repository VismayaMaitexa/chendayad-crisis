# Generated by Django 5.1.4 on 2025-01-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0019_remove_admindonation_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admindonation',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
