# Generated by Django 5.0.1 on 2024-02-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='available_time',
        ),
        migrations.AddField(
            model_name='doctor',
            name='avail_time',
            field=models.ManyToManyField(to='doctor.availabletime'),
        ),
    ]
