# Generated by Django 5.1.4 on 2024-12-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0004_crisisreporting_delete_crisisreports'),
    ]

    operations = [
        migrations.CreateModel(
            name='admindetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=20)),
                ('password', models.CharField(default='password', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='crisisreporting',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
