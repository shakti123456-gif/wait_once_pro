# Generated by Django 4.2 on 2024-06-05 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_api_user', '0013_alter_user_mobile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_mobile',
            name='Dateofbirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_mobile',
            name='email_address',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
