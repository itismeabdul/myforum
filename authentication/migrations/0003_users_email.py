# Generated by Django 3.1 on 2020-08-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_users_activated'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
