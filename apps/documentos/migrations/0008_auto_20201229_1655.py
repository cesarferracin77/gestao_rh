# Generated by Django 3.1.4 on 2020-12-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0007_auto_20201229_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='imagem',
            field=models.ImageField(default=1, upload_to='documentos/imagens'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(upload_to='documentos/pdfs'),
        ),
    ]
