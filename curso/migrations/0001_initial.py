# Generated by Django 2.2.5 on 2020-08-31 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='NOME')),
                ('descricao', models.CharField(max_length=150, verbose_name='DESCRIÇÃO')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('qtd_horas', models.CharField(max_length=5, verbose_name='Quantidade de Horas')),
                ('local', models.CharField(max_length=155, verbose_name='LOCAL')),
                ('data', models.CharField(max_length=5, verbose_name='Data')),
                ('hora', models.CharField(max_length=5, verbose_name='Hora')),
                ('status', models.BooleanField(default=False, verbose_name='STATUS')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CursoComentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='NOME')),
                ('descricao', models.CharField(max_length=150, verbose_name='DESCRIÇÃO')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.Curso')),
            ],
        ),
    ]
