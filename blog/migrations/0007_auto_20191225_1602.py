# Generated by Django 3.0 on 2019-12-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191219_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='brief',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]