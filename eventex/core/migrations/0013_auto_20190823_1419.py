# Generated by Django 2.0.6 on 2019-08-23 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_course_abc_to_mti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseold',
            name='speakers',
        ),
        migrations.DeleteModel(
            name='CourseOld',
        ),
    ]
