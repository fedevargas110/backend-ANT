# Generated by Django 2.2.7 on 2019-11-20 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LISTA', '0002_guest_attended'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Guest',
            new_name='People',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='id_guest',
            new_name='id_people',
        ),
    ]