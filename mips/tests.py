from django.test import TestCase
from models import Mip

import os
import django

# set the DJANGO_SETTINGS_MODULE environment variable to "mips.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")

# setup
django.setup()


# models test
class MipTestCase(TestCase):
    def setUp(self):
        o = Mip.objects.create(mip_id=1, mip_start=1, mip_stop=2)
        o.save()

    def test_mip_id_repr(self):
        mip1 = Mip.objects.get(mip_id=1)
        self.assertEqual(mip1.__unicode__(), u'1')
