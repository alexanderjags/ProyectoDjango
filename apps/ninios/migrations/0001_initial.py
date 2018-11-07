# Generated by Django 2.1.3 on 2018-11-06 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adopciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aportacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_ayuda', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ninio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('fecha_nac', models.DateField(blank=True)),
                ('edad', models.IntegerField()),
                ('aportacion', models.ManyToManyField(blank=True, to='ninios.Aportacion')),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopciones.Persona')),
            ],
        ),
    ]