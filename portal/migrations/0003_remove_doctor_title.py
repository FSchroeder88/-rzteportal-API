# Generated by Django 4.1.2 on 2022-10-16 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_appointment_created_at_alter_appointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='title',
        ),
    ]
