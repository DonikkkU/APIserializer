# Generated by Django 4.0.6 on 2022-08-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
