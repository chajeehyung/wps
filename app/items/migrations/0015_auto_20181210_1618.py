# Generated by Django 2.1.3 on 2018-12-10 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='ingredient',
            field=models.TextField(max_length=10000),
        ),
    ]
