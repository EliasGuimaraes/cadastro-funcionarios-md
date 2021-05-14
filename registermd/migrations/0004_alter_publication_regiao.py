# Generated by Django 3.2 on 2021-05-13 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registermd', '0003_alter_publication_regiao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='regiao',
            field=models.CharField(choices=[('brasil', 'BRASIL'), ('norla', 'NORLA'), ('conosur', 'CONOSUR')], default='brasil', max_length=7),
        ),
    ]
