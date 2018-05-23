# Generated by Django 2.0.4 on 2018-05-22 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formentry', '0009_auto_20180517_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='formEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.CharField(max_length=150, verbose_name='उत्तर')),
                ('member', models.IntegerField(verbose_name='आइ डी')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formentry.formValue')),
                ('formfield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formentry.questions')),
            ],
        ),
        migrations.CreateModel(
            name='MarkValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marker', models.CharField(max_length=40, verbose_name='प्रश्नकर्ता')),
                ('marks', models.FloatField(verbose_name='Marks')),
                ('valueid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postform.formEntries')),
            ],
        ),
    ]
