# Generated by Django 3.2 on 2021-05-13 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registermd', '0005_alter_publication_regiao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='regiao',
            field=models.CharField(choices=[('BRASIL', 'BRASIL'), ('NORLA', 'NORLA'), ('CONOSUR', 'CONOSUR')], max_length=7),
        ),
    ]
