# Generated by Django 4.2.5 on 2023-11-22 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]