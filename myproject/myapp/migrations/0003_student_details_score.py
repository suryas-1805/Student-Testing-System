# Generated by Django 5.0 on 2023-12-11 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_student_name_student_details_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='score',
            field=models.IntegerField(default=True),
        ),
    ]
