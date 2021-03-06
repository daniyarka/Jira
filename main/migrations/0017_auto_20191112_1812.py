# Generated by Django 2.2.5 on 2019-11-12 18:12

from django.db import migrations, models
import utils.upload
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20191112_1804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='taskdocument',
            name='document',
            field=models.FileField(upload_to=utils.upload.document_path, validators=[utils.validators.validate_file_size, utils.validators.validate_extension]),
        ),
    ]
