# Generated by Django 3.1.6 on 2021-03-20 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['num_pages'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='journal',
            options={'verbose_name': 'Журнал', 'verbose_name_plural': 'Журналы'},
        ),
    ]