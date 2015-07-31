import os
import django

# set the DJANGO_SETTINGS_MODULE environment variable to "mips.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")

# setup
django.setup()

from django.test import TestCase
from models import Mip, Instance
import datetime


class MipTestCase(TestCase):
    def setUp(self):
        o = Mip.objects.create(mip_id=1, mip_start=1, mip_stop=2)
        o.save()

    def test_mip_id_repr(self):
        mip1 = Mip.objects.get(mip_id=1)
        self.assertEqual(mip1.__unicode__(), u'1')


class InstanceTestCase(TestCase):
    def setUp(self):
        m = Mip.objects.create(mip_id=1, mip_start=1, mip_stop=2)
        m.save()

        o = Instance.objects.create(mip_fk=m, mip_pool=1, mip_instance=1, mip_production_data=datetime.datetime.now())
        o.save()

    def test_instance_repr(self):
        m = Mip.objects.get(mip_id=1)
        o = Instance.objects.get(mip_fk=m, mip_instance=1)

        self.assertEqual(o.__unicode__(), u'mip|mip_instance: 1|1')
