# Generated by Django 4.2.3 on 2023-09-03 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
