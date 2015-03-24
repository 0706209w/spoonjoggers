# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawcrastination', '0005_remove_picture_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(default=b'', to='pawcrastination.AnimalProfile'),
            preserve_default=True,
        ),
    ]
