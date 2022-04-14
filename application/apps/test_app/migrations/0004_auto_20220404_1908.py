# Generated by Django 3.2.12 on 2022-04-04 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20220404_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedulebus',
            name='ap_minsk',
        ),
        migrations.RemoveField(
            model_name='schedulebus',
            name='ap_minsk_weekend',
        ),
        migrations.RemoveField(
            model_name='schedulebus',
            name='city_bus',
        ),
        migrations.RemoveField(
            model_name='schedulebus',
            name='sovetskaya_minsk',
        ),
        migrations.RemoveField(
            model_name='schedulebus',
            name='sovetskaya_minsk_weekend',
        ),
        migrations.AddField(
            model_name='schedulebus',
            name='weekend',
            field=models.TextField(default=1, verbose_name='Выходные'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedulebus',
            name='work_days',
            field=models.TextField(default=1, verbose_name='Рабочие дни'),
            preserve_default=False,
        ),
    ]