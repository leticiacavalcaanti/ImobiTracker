# Generated by Django 5.1.2 on 2024-10-20 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='creci',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
