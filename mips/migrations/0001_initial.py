# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('mip_pool', models.IntegerField()),
                ('mip_production_data', models.DateField()),
                ('mip_producer', models.CharField(max_length=255)),
                ('mip_plate', models.CharField(max_length=255)),
                ('mip_position', models.CharField(max_length=50)),
                ('mip_instance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mip',
            fields=[
                ('mip_id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('mip_sequence', models.TextField()),
                ('mip_extension_arm', models.TextField()),
                ('mip_ligation_arm', models.TextField()),
                ('mip_func_immuno', models.BooleanField(default=False)),
                ('mip_func_mapping', models.BooleanField(default=False)),
                ('mip_func_random', models.BooleanField(default=False)),
                ('mip_func_utr', models.BooleanField(default=False)),
                ('mip_start', models.IntegerField()),
                ('mip_stop', models.IntegerField()),
                ('mip_comments', models.TextField()),
                ('reference_id', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paralog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('subspecies', models.CharField(max_length=100)),
                ('mip_subspecies_paralog', models.CharField(max_length=50)),
                ('mip_id_fk', models.ForeignKey(to='mips.Mip')),
            ],
        ),
        migrations.CreateModel(
            name='Samples',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('mip_sequence', models.TextField()),
                ('mip_performance', models.BooleanField(default=False)),
                ('mip_id_fk', models.ForeignKey(to='mips.Mip')),
            ],
        ),
        migrations.CreateModel(
            name='SampleSpecies',
            fields=[
                ('sample_id', models.IntegerField(serialize=False, primary_key=True)),
                ('subspecies', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='samples',
            name='sample_id_fk',
            field=models.ForeignKey(to='mips.SampleSpecies'),
        ),
        migrations.AddField(
            model_name='instance',
            name='mip_id_fk',
            field=models.ForeignKey(to='mips.Mip'),
        ),
    ]
