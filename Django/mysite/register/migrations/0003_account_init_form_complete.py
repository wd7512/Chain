# Generated by Django 3.1.4 on 2021-01-23 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20210105_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='init_form_complete',
            field=models.BooleanField(default=False),
        ),
    ]
