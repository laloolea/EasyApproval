# Generated by Django 2.1.3 on 2019-12-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_auto_20191210_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/contancias'),
        ),
    ]
