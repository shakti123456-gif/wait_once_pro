# Generated by Django 4.2 on 2024-06-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_api_user', '0010_alter_service_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='Therapist',
            field=models.ManyToManyField(blank=True, to='mobile_api_user.therapist'),
        ),
    ]
