# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0012_auto_20150712_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='NoticeContent',
            field=models.TextField(default=b'NA'),
        ),
    ]
