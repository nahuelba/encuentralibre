# Generated by Django 3.0.8 on 2020-07-14 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiforms', '0003_auto_20200712_1931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resultado',
            options={'ordering': ['-fecha']},
        ),
    ]
