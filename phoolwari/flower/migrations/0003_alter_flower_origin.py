# Generated by Django 4.2.3 on 2023-11-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0002_alter_category_options_category_image_flower_origin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='origin',
            field=models.CharField(default='india', max_length=100),
        ),
    ]
