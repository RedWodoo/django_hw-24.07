# Generated by Django 5.0.7 on 2024-07-23 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_rubric_bb_rubric'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roditel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Rebenok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(blank=True, choices=[(None, 'Выберите тип rebenka'), ('b', 'Son'), ('s', 'Daughter')], max_length=1)),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('title', models.CharField(max_length=50, verbose_name='Rebenok')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('roditel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.roditel', verbose_name='Roditel')),
            ],
            options={
                'verbose_name': 'Rebenok',
                'verbose_name_plural': 'Rebenki',
                'ordering': ['-published', 'title'],
            },
        ),
        migrations.DeleteModel(
            name='Bb',
        ),
        migrations.DeleteModel(
            name='Rubric',
        ),
    ]
