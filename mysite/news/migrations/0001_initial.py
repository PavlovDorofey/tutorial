# Generated by Django 4.2.5 on 2023-12-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=75, verbose_name='Название')),
                ('anons', models.CharField(default='', max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(default='', max_length=2500, verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
