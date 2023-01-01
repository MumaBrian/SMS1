# Generated by Django 4.1.3 on 2022-11-13 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
        ('classinfo', '0001_initial'),
        ('student', '0002_studentinfo_classroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classinfo.classinfo')),
                ('student', models.ManyToManyField(to='student.studentinfo')),
                ('teacher', models.ManyToManyField(to='teacher.teacherinfo')),
            ],
        ),
    ]
