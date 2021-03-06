# Generated by Django 3.1 on 2020-09-22 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20200914_0711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sportsection',
            options={'verbose_name': 'Секция', 'verbose_name_plural': 'Спортивные секции'},
        ),
        migrations.AddField(
            model_name='sportsection',
            name='long_description',
            field=models.TextField(blank=True, verbose_name='Описание секции'),
        ),
        migrations.AddField(
            model_name='sportsection',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255, verbose_name='Название секции'), verbose_name='Slug поле'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.sportsection', verbose_name='Спортивная секция'),
        ),
    ]
