# Generated by Django 3.1.1 on 2021-05-17 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0012_remove_crypto_image_ori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crypto',
            name='psnr',
        ),
    ]
