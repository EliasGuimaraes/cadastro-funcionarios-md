# Generated by Django 3.2 on 2021-05-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registermd', '0004_alter_publication_regiao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='regiao',
            field=models.CharField(max_length=7),
        ),
    ]