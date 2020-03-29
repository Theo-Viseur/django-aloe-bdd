# Generated by Django 3.0.4 on 2020-03-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED')], default='PENDING', max_length=8),
        ),
    ]
