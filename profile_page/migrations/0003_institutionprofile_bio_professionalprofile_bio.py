# Generated by Django 5.0.7 on 2025-05-29 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0002_alter_institutionprofile_professionals_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutionprofile',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='professionalprofile',
            name='bio',
            field=models.TextField(default=''),
        ),
    ]
