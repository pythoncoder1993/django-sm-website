# Generated by Django 4.2.3 on 2023-07-13 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_samplemarksheetinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplemarksheetinformation',
            name='teacher_marks_choices',
            field=models.CharField(choices=[('1', 'Good'), ('2', 'Average'), ('3', 'Belowaverage')], default=1, max_length=30),
        ),
    ]