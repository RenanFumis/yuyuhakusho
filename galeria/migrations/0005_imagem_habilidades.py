# Generated by Django 5.0.6 on 2024-06-03 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_alter_imagem_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagem',
            name='habilidades',
            field=models.CharField(default='Habilidade', max_length=200),
            preserve_default=False,
        ),
    ]
