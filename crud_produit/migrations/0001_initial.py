# Generated by Django 5.1.7 on 2025-05-07 14:49

import crud_produit.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=100)),
                ('categorie', models.CharField(choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Food', 'Food'), ('Books', 'Books'), ('Other', 'Other')], max_length=122)),
                ('quantite', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=crud_produit.models.file_path)),
                ('description', models.TextField(blank=True)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
