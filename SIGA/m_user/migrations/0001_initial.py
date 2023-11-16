# Generated by Django 4.2.6 on 2023-11-16 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('num_rut', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('pnombre', models.CharField(max_length=30)),
                ('snombre', models.CharField(blank=True, max_length=30, null=True)),
                ('appat', models.CharField(max_length=30)),
                ('apmat', models.CharField(max_length=30)),
                ('fec_nac', models.DateField()),
                ('nacionalidad', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
                ('genero', models.IntegerField(choices=[[0, 'Femenino'], [1, 'Masculino'], [2, 'No aplica']])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('numero', models.IntegerField()),
            ],
            options={
                'db_table': 'Apoderado',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Usuario',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('num_rut', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('pnombre', models.CharField(max_length=30)),
                ('snombre', models.CharField(blank=True, max_length=30, null=True)),
                ('appat', models.CharField(max_length=30)),
                ('apmat', models.CharField(max_length=30)),
                ('fec_nac', models.DateField()),
                ('nacionalidad', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
                ('genero', models.IntegerField(choices=[[0, 'Femenino'], [1, 'Masculino'], [2, 'No aplica']])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('numero', models.IntegerField()),
                ('parentezco', models.CharField(max_length=10)),
                ('Apoderado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m_user.apoderado')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='m_user.usuario')),
            ],
            options={
                'db_table': 'Estudiante',
            },
        ),
        migrations.AddField(
            model_name='apoderado',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='m_user.usuario'),
        ),
    ]
