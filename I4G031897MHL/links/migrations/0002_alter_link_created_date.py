# Generated by Django 4.0.5 on 2022-07-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]
