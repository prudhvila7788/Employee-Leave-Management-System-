# Generated by Django 2.1 on 2018-11-26 05:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0023_auto_20181126_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 26, 11, 2, 19, 989096), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='leave_app_id',
            field=models.IntegerField(unique=True),
        ),
    ]
