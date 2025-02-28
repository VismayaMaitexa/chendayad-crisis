# Generated by Django 5.1.4 on 2024-12-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=20)),
                ('password', models.CharField(default='password', max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='volunteerdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=20)),
                ('password', models.CharField(default='password', max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('bloodgroup', models.CharField(max_length=20)),
            ],
        ),
    ]
