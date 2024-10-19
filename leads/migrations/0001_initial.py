# Generated by Django 5.0 on 2024-10-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=45)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('anotacao', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
