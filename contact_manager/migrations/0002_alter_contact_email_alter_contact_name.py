# Generated by Django 5.0 on 2023-12-13 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]