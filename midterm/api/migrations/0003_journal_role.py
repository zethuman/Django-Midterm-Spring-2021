# Generated by Django 3.1.6 on 2021-03-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210320_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='role',
            field=models.SmallIntegerField(choices=[(1, 'BULLET'), (2, 'FOOD'), (3, 'TRAVEL'), (4, 'SPORT')], default=1),
        ),
    ]
