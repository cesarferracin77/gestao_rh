# Generated by Django 3.1.4 on 2020-12-29 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0006_auto_20201229_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(upload_to='documentos/'),
        ),
    ]
