# Generated by Django 4.2.1 on 2023-05-19 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Personalidade',
                'verbose_name_plural': 'Personalidades',
            },
        ),
        migrations.CreateModel(
            name='Atores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=50)),
                ('segundo_nome', models.CharField(max_length=50)),
                ('idade', models.CharField(max_length=50)),
                ('show', models.BooleanField(default=True)),
                ('imagem', models.ImageField(blank=True, upload_to='pictures/%Y/%m/')),
                ('link_videos', models.CharField(max_length=255)),
                ('personalidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.personalidade')),
            ],
            options={
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
            },
        ),
    ]
