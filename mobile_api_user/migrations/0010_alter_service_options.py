# Generated by Django 4.2 on 2024-05-31 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_api_user', '0009_alter_customerdetails_options_alter_service_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'managed': True, 'ordering': ['service_id'], 'verbose_name': 'Services', 'verbose_name_plural': 'Services'},
        ),
    ]
