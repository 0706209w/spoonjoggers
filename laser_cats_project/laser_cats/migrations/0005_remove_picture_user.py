# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laser_cats', '0004_picture_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='user',
        ),
    ]
