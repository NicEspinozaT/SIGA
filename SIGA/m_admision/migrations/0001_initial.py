# Generated by Django 4.2.6 on 2023-11-19 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('m_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('estado', models.IntegerField(choices=[[0, 'No Pagado'], [1, 'Pendiente'], [2, 'Pagado']])),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('periodo', models.IntegerField(default=2023)),
                ('Apoderado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m_user.apoderado')),
                ('Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m_user.estudiante')),
            ],
            options={
                'db_table': 'Matricula',
            },
        ),
    ]
