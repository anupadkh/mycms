# Generated by Django 2.0.4 on 2018-05-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formentry', '0008_questionchoice_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionchoice',
            name='sub_question',
        ),
        migrations.AlterField(
            model_name='questionchoice',
            name='choiceMarks',
            field=models.TextField(blank=True, null=True, verbose_name='Choice Marks'),
        ),
    ]
