# Generated by Django 4.2.17 on 2025-02-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_class_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='照片'),
        ),
    ]
