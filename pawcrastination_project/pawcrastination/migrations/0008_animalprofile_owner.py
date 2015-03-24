# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawcrastination', '0007_auto_20150320_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalprofile',
            name='owner',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
