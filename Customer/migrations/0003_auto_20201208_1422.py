# Generated by Django 3.1.3 on 2020-12-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_auto_20201207_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
