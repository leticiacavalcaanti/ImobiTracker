# Generated by Django 5.0 on 2024-10-10 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leads', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('dataInclusao', models.DateTimeField(auto_now_add=True)),
                ('previsaoVenda', models.DateField()),
                ('vencimentoAtualizacao', models.DateField()),
                ('dataFechamento', models.DateField(blank=True, null=True)),
                ('etapa', models.CharField(max_length=45)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.lead')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
    ]
