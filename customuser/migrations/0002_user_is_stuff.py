# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_stuff',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
