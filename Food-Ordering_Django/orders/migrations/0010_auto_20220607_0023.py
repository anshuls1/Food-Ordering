# Generated by Django 2.2.7 on 2022-06-06 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_savedcarts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DinnerPlatters',
            new_name='Drinks',
        ),
    ]