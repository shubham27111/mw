# Generated by Django 3.0.7 on 2020-06-26 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200626_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='items_jason',
            new_name='items_json',
        ),
    ]