# Generated by Django 4.1.1 on 2022-11-02 00:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_bank_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=500)),
                ('is_active', models.BooleanField(default=False)),
                ('is_seen', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('to_leader', models.ManyToManyField(blank=True, related_name='to_leader', to=settings.AUTH_USER_MODEL)),
                ('to_worker', models.ManyToManyField(blank=True, related_name='to_worker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
