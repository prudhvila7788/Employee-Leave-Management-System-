# Generated by Django 2.1 on 2018-11-26 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0024_auto_20181126_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaveapplication',
            name='id',
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 26, 11, 39, 4, 772925), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='leave_app_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
