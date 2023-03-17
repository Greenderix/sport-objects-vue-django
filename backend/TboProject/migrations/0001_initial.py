# Generated by Django 4.1.7 on 2023-03-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectLocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('activ', models.CharField(max_length=2, verbose_name='activ')),
                ('discShort', models.CharField(max_length=700, verbose_name='discShort')),
                ('discLong', models.CharField(max_length=1000, verbose_name='discLong')),
                ('addres', models.CharField(max_length=100, verbose_name='addres')),
                ('oktmo', models.IntegerField(null=True, verbose_name='oktmo')),
                ('fcp', models.CharField(max_length=30, verbose_name='fcp')),
                ('actions', models.CharField(max_length=50, verbose_name='actions')),
                ('startBuild', models.CharField(max_length=50, verbose_name='startBuild')),
                ('endBuild', models.CharField(max_length=50, verbose_name='endBuild')),
                ('finValue', models.IntegerField(null=True, verbose_name='finValue')),
                ('curator', models.CharField(max_length=100, verbose_name='curator')),
                ('telephone', models.CharField(max_length=100, verbose_name='telephone')),
                ('workHours', models.CharField(max_length=100, verbose_name='workHours')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('siteUrl', models.CharField(max_length=100, verbose_name='siteUrl')),
                ('typeObject', models.CharField(max_length=100, verbose_name='typeObject')),
                ('typeSport', models.CharField(max_length=100, verbose_name='typeSport')),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('scaleMap', models.IntegerField(null=True, verbose_name='scaleMap')),
                ('photoUrl', models.CharField(max_length=50, verbose_name='photoUrl')),
            ],
        ),
    ]
