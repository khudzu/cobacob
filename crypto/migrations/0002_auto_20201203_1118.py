# Generated by Django 3.1.1 on 2020-12-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='action',
            field=models.CharField(choices=[('ENKRIPSI', 'Enkripsi'), ('DEKRIPSI', 'Dekripsi')], default='ENKRIPSI', max_length=50),
        ),
    ]
