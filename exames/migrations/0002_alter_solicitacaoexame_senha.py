# Generated by Django 5.1 on 2024-09-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacaoexame',
            name='senha',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
