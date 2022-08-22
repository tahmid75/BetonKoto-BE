# Generated by Django 3.2.10 on 2022-01-20 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0002_level'),
        ('profiles', '0005_auto_20220114_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='band',
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='position.level'),
        ),
        migrations.DeleteModel(
            name='Band',
        ),
    ]