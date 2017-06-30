# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db.models.functions import Length
from django.test import TestCase

from .models import Feature


class GisBugTests(TestCase):

    def test_gis_bug(self):
        """
        The test tries to make a query.
        """
        features = Feature.objects.annotate(length=Length('shape'))
        # This action adds an additional parameter to the st_lengthspheroid
        # function every time you call the str function on the queryset
        str(features.query)
        # As a result it raises ProgrammingError, but it must pass without an error.
        features.first()
