# Generated by Django 4.1.2 on 2022-10-18 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tipo_post',
            field=models.CharField(choices=[('Exp', 'Experiencia'), ('Edu', 'Educacion'), ('Hab', 'Habilidades'), ('Pro', 'Projectos'), ('Cer', 'Certificaciones')], default=('Exp', 'Experiencia'), max_length=3),
        ),
    ]
