# Generated by Django 2.2.7 on 2019-11-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlgApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='description',
            field=models.TextField(default=' '),
        ),
    ]
