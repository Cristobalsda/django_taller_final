# Generated by Django 4.1 on 2022-12-21 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=40)),
                ('fechaInscripcion', models.DateTimeField()),
                ('institucion', models.CharField(max_length=40)),
                ('horaInscripcion', models.TimeField()),
                ('estado', models.CharField(max_length=20)),
                ('observacion', models.CharField(max_length=255)),
            ],
        ),
    ]
