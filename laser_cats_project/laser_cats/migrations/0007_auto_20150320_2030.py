# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laser_cats', '0006_picture_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='animalType',
            field=models.CharField(default=b'othr', max_length=4, choices=[(b'dog', b'dog'), (b'cat', b'cat'), (b'bnny', b'bunny'), (b'hrse', b'horse'), (b'fish', b'fish'), (b'bird', b'bird'), (b'rptl', b'reptile'), (b'othr', b'any other')]),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to=b'/images/', blank=True),
        ),
    ]
