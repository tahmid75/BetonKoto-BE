# Generated by Django 3.2.10 on 2022-01-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
