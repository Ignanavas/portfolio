# Generated by Django 4.1.2 on 2022-10-18 03:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tipo_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fin_fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='inicio_fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
