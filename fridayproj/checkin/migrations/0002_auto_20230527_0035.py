# Generated by Django 4.2.1 on 2023-05-27 07:35

from django.db import migrations

def create_data(apps, schema_editor):
    Member = apps.get_model('checkin', 'Member')
    Member(name='Ben Hogan', email='ben@hoge.com', document='63565', phone='5555555').save()


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
    ]

    operations = [
    migrations.RunPython(create_data)
    ]
