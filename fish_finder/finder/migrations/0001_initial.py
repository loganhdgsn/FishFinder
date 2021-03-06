# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-14 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('waterBody', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('accessType', models.CharField(max_length=50)),
                ('boatSize', models.CharField(max_length=50)),
                ('rampType', models.CharField(max_length=50)),
                ('universalAccess', models.CharField(max_length=50)),
                ('bulletinBoard', models.CharField(max_length=50)),
                ('exposure', models.CharField(max_length=50)),
                ('parking', models.CharField(max_length=50)),
                ('shorefishing', models.CharField(max_length=50)),
                ('useVolume', models.CharField(max_length=50)),
                ('dock', models.CharField(max_length=50)),
                ('winterPlowing', models.CharField(max_length=50)),
                ('summerPortolet', models.CharField(max_length=50)),
                ('winterPortolet', models.CharField(max_length=50)),
                ('tempPortolet', models.CharField(max_length=50)),
                ('accessName', models.CharField(max_length=50)),
                ('bowfin', models.CharField(max_length=50)),
                ('carp', models.CharField(max_length=50)),
                ('channelCatfish', models.CharField(max_length=50)),
                ('whiteCrappie', models.CharField(max_length=50)),
                ('longnoseGar', models.CharField(max_length=50)),
                ('muskellunge', models.CharField(max_length=50)),
                ('whitePerch', models.CharField(max_length=50)),
                ('americanShad', models.CharField(max_length=50)),
                ('sheepshead', models.CharField(max_length=50)),
                ('lakeWhitefish', models.CharField(max_length=50)),
                ('brookTrout', models.CharField(max_length=50)),
                ('brownTrout', models.CharField(max_length=50)),
                ('rainbowTrout', models.CharField(max_length=50)),
                ('lakeTrout', models.CharField(max_length=50)),
                ('landlockedSalmon', models.CharField(max_length=50)),
                ('rainbowSmelt', models.CharField(max_length=50)),
                ('yellowPerch', models.CharField(max_length=50)),
                ('walleye', models.CharField(max_length=50)),
                ('northernPike', models.CharField(max_length=50)),
                ('chainPickerel', models.CharField(max_length=50)),
                ('largemouthBass', models.CharField(max_length=50)),
                ('smallmouthBass', models.CharField(max_length=50)),
                ('bullhead', models.CharField(max_length=50)),
                ('panfish', models.CharField(max_length=50)),
                ('blackCrappie', models.CharField(max_length=50)),
                ('burbot', models.CharField(max_length=50)),
                ('coordX', models.DecimalField(decimal_places=10, max_digits=13)),
                ('coordY', models.DecimalField(decimal_places=10, max_digits=13)),
            ],
        ),
    ]
