# Generated by Django 3.1.4 on 2020-12-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_detailbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailbook',
            name='book',
        ),
        migrations.AddField(
            model_name='detailbook',
            name='book',
            field=models.ManyToManyField(to='book.Book', verbose_name='Lista de libros'),
        ),
    ]
