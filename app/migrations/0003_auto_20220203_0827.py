# Generated by Django 3.2.12 on 2022-02-03 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220203_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='stu',
            name='section',
            field=models.CharField(max_length=200),
        ),
    ]
