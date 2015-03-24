# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawcrastination', '0009_auto_20150323_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalprofile',
            name='animalType',
            field=models.CharField(default=b'Others', max_length=8, choices=[(b'Dogs', b'Dogs'), (b'Cats', b'Cats'), (b'Bunnies', b'Bunnies'), (b'Horses', b'Horses'), (b'Fish', b'Fish'), (b'Birds', b'Birds'), (b'Reptiles', b'Reptiles'), (b'Others', b'Others')]),
        ),
    ]
