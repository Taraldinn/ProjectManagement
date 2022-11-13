# Generated by Django 4.1.1 on 2022-11-12 20:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0005_alter_paymentprojectbased_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentprojectbased',
            name='receivers',
            field=models.ManyToManyField(blank=True, related_name='worker_payments', to=settings.AUTH_USER_MODEL),
        ),
    ]