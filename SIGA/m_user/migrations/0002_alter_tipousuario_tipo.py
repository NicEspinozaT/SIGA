# Generated by Django 4.2.6 on 2023-11-15 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipousuario',
            name='tipo',
            field=models.CharField(max_length=15),
        ),
    ]