# Generated by Django 5.0.3 on 2024-03-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escritor',
            name='biografia',
            field=models.TextField(null=True),
        ),
    ]