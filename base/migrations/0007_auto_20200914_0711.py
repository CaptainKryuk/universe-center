# Generated by Django 3.1 on 2020-09-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_coach_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='rank',
            field=models.CharField(max_length=255, verbose_name='Позиция тренера'),
        ),
    ]
