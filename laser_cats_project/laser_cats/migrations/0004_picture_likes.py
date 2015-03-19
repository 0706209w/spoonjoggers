# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laser_cats', '0003_auto_20150319_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
