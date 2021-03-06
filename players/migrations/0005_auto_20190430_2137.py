# Generated by Django 2.0.13 on 2019-04-30 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20190407_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='players',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='players',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='players',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
