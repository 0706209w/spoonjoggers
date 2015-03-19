# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laser_cats', '0002_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(to='laser_cats.AnimalProfile'),
        ),
    ]
