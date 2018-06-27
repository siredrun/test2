# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20180626_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='btitile',
            new_name='btitle',
        ),
    ]
