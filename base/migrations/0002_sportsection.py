# Generated by Django 3.1 on 2020-09-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название секции')),
                ('description', models.CharField(max_length=255, verbose_name='Описание секции')),
                ('icon', models.ImageField(upload_to='sections', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Секция',
                'verbose_name_plural': "Секции из раздела 'Мы помогаем вашим детям...'",
            },
        ),
    ]
