# Generated by Django 3.2.11 on 2022-01-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('roll_no', models.IntegerField()),
                ('section', models.CharField(max_length=1)),
            ],
        ),
    ]
