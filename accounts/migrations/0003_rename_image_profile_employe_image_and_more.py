# Generated by Django 4.1.1 on 2022-10-18 22:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='employe_image',
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='fathers_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='marital_Status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='mothers_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='nationality',
            field=models.CharField(default=django.utils.timezone.now, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='nid_card_no',
            field=models.CharField(default=django.utils.timezone.now, max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='postel_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='sex_name',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Others')], default=django.utils.timezone.now, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='surname',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]