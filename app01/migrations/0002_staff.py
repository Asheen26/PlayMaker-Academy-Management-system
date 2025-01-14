# Generated by Django 5.1.4 on 2025-01-13 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('profile_photo', models.ImageField(upload_to='plyrprof')),
                ('contact', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
