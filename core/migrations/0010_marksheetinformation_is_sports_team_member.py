# Generated by Django 4.2.3 on 2023-07-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_marksheetinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='marksheetinformation',
            name='is_sports_team_member',
            field=models.BooleanField(default=False),
        ),
    ]