# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laser_cats', '0005_remove_picture_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(default=b'', to='laser_cats.AnimalProfile'),
            preserve_default=True,
        ),
    ]
