# Generated by Django 3.2 on 2023-02-10 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_menu', '0008_menuitem_subpage_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='subpage_key',
            new_name='subpage_url',
        ),
    ]
