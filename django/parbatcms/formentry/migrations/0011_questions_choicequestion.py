# Generated by Django 2.0.4 on 2018-05-26 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formentry', '0010_auto_20180524_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='choicequestion',
            field=models.IntegerField(blank=True, null=True, verbose_name='Parent Choices'),
        ),
    ]