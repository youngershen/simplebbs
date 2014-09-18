# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import customuser.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=255)),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('avatar', models.ImageField(null=True, upload_to=customuser.models._get_file_dir, blank=True)),
                ('gender', models.CharField(default=b'unknown', max_length=10, choices=[(b'male', b'male'), (b'female', b'female'), (b'shemale', b'shemale'), (b'unknown', b'unknown')])),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('modified_time', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': 'users',
            },
            bases=(models.Model,),
        ),
    ]
