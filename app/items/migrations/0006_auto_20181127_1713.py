# Generated by Django 2.1.3 on 2018-11-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_category_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='photo',
            field=models.ImageField(max_length=300, upload_to='ItemImage'),
        ),
    ]
