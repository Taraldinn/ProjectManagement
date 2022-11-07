# Generated by Django 4.1.1 on 2022-11-07 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_alter_issues_total_data_entry_today'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='accept_status',
            field=models.CharField(choices=[('draft', 'draft'), ('decline', 'decline'), ('accept', 'accept')], default=('draft', 'draft'), max_length=15),
        ),
    ]
