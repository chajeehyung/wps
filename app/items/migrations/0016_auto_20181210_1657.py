# Generated by Django 2.1.3 on 2018-12-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_auto_20181210_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='dom',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='description',
            name='ingredient',
            field=models.TextField(),
        ),
    ]
