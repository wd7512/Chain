# Generated by Django 3.1.4 on 2021-01-24 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promoters', '0006_auto_20210124_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_form',
            name='email',
        ),
        migrations.AddField(
            model_name='user_form',
            name='email2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
