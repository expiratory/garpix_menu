# Generated by Django 3.1 on 2021-10-20 07:36

from django.db import migrations, models
import garpix_menu.validators
import garpix_utils.file.file_field


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_menu', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='icon',
            field=models.FileField(blank=True, default='', upload_to=garpix_utils.file.file_field.get_file_path, validators=[garpix_menu.validators.validate_type, garpix_menu.validators.validate_size], verbose_name='Иконка'),
        ),
    ]
