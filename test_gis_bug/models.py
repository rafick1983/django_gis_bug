# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Feature(models.Model):
    shape = models.LineStringField()
