# Generated by Django 4.0.4 on 2022-05-23 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0001_initial'),
        ('start_trails', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StartingPoint',
            new_name='StartTrail',
        ),
        migrations.RenameField(
            model_name='starttrail',
            old_name='startLat',
            new_name='start_lat',
        ),
        migrations.RenameField(
            model_name='starttrail',
            old_name='startLng',
            new_name='start_lng',
        ),
    ]
