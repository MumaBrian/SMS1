# Generated by Django 4.1.3 on 2022-12-24 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0001_initial'),
        ('classinfo', '0001_initial'),
        ('subjectinfo', '0002_rename_me_subjectinfo_classroom'),
        ('student', '0010_student_exam_score_student_test_score'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='StudentModel',
        ),
    ]