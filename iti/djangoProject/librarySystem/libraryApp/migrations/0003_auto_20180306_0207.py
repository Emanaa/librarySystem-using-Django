# Generated by Django 2.0 on 2018-03-06 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0002_auto_20180306_0146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='writer',
            old_name='profile_pic',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='writer',
            old_name='bornAt',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='writer',
            old_name='diedAt',
            new_name='date_of_death',
        ),
    ]
