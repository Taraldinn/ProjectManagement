# Generated by Django 4.1.1 on 2022-10-26 00:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_sort_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='complete_per',
            field=models.FloatField(blank=True, max_length=2, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_client_budget',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_eastemate_cost',
            field=models.IntegerField(default=0),
        ),
    ]