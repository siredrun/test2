# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20180626_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='bcoment',
            new_name='bcommet',
        ),
    ]
