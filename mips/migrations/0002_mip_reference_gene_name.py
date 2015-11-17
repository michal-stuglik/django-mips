# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mip',
            name='reference_gene_name',
            field=models.TextField(null=True),
        ),
    ]
