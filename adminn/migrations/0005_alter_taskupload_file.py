# Generated by Django 4.1.3 on 2022-12-20 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminn', '0004_taskupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskupload',
            name='file',
            field=models.CharField(max_length=500),
        ),
    ]
