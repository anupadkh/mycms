# Generated by Django 2.0.4 on 2018-05-13 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr_type', models.IntegerField(default=1, verbose_name='Temporary or Permanent')),
                ('country', models.CharField(default='Nepal', max_length=20, verbose_name='Country')),
                ('district', models.CharField(max_length=40, verbose_name='District')),
                ('house', models.IntegerField(blank=True, null=True, verbose_name='House No')),
                ('palika', models.CharField(max_length=20, verbose_name='Municipality')),
                ('state', models.CharField(max_length=30, verbose_name='State')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('contact_type', models.IntegerField(default=1, verbose_name='Type of Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gened', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeoCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=30, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=30, verbose_name='Longitude')),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=50)),
                ('timespent', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.GeoCode')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personal.Family')),
            ],
        ),
        migrations.CreateModel(
            name='Nagrikta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('reg_date', models.CharField(max_length=10)),
                ('card_type', models.IntegerField(default=1, verbose_name='Type of Card')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, verbose_name='First Name')),
                ('lname', models.CharField(max_length=100, verbose_name='Last Name')),
                ('mname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Middle Name')),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('gened', models.CharField(blank=True, default='23', max_length=60, null=True, verbose_name='Generated Id')),
                ('creator', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relntype', models.CharField(max_length=50)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationhead', to='personal.Family')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('social_type', models.IntegerField(default=1, verbose_name='Media Type')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Personal')),
            ],
        ),
        migrations.AddField(
            model_name='nagrikta',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Personal'),
        ),
        migrations.AddField(
            model_name='hobby',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Personal'),
        ),
        migrations.AddField(
            model_name='family',
            name='myhouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.GeoCode'),
        ),
        migrations.AddField(
            model_name='family',
            name='person_head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Personal'),
        ),
        migrations.AddField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Personal'),
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Personal'),
        ),
    ]