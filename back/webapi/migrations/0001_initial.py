# Generated by Django 2.1.7 on 2019-02-15 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmClock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
                ('hour', models.IntegerField()),
                ('minute', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('auto_stop_minutes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BackupMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backup_file', models.FileField(upload_to='backup_mp3')),
            ],
        ),
        migrations.CreateModel(
            name='WebRadio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=250)),
                ('is_default', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='alarmclock',
            name='webradio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapi.WebRadio'),
        ),
    ]
