# Generated by Django 3.1.6 on 2021-03-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210320_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='type',
            field=models.CharField(choices=[('BULLET', 'BULLET'), ('FOOD', 'FOOD'), ('TRAVEL', 'TRAVEL'), ('SPORT', 'SPORT')], default='BULLET', max_length=255, verbose_name='Типы'),
        ),
    ]
