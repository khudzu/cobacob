# Generated by Django 3.1.1 on 2020-12-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0005_auto_20201203_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]
