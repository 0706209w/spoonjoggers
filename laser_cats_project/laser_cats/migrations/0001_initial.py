# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('animalType', models.CharField(default=b'othr', max_length=4, choices=[(b'dog', b'dog'), (b'cat', b'cat'), (b'hrse', b'horse'), (b'fish', b'fish'), (b'bird', b'bird'), (b'rptl', b'reptile'), (b'othr', b'any other')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
