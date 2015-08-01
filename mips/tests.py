import os
import django
import datetime

# set the DJANGO_SETTINGS_MODULE environment variable to "mips.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")

# setup
django.setup()

from django.test import TestCase
from models import Mip, Instance, Subspecies, SampleSubspecies, Samples, Paralog


class MipTest(TestCase):
    def setUp(self):
        o = Mip.objects.create(mip_id=1, mip_start=1, mip_stop=2)

    def test_unicode(self):
        mip1 = Mip.objects.get(mip_id=1)
        self.assertTrue(isinstance(mip1, Mip))
        self.assertEqual(mip1.__unicode__(), u'1')


class InstanceTest(TestCase):
    def setUp(self):
        m = Mip.objects.create(mip_id=1, mip_start=1, mip_stop=2)
        o = Instance.objects.create(mip_fk=m, mip_pool=1, mip_instance=1, mip_production_data=datetime.datetime.now())

    def test_unicode(self):
        m = Mip.objects.get(mip_id=1)
        o = Instance.objects.get(mip_fk=m, mip_instance=1)
        self.assertEqual(o.__unicode__(), u'mip|mip_instance: 1|1')


class SubspeciesTest(TestCase):
    def setUp(self):
        o = Subspecies.objects.create(subspecies='LV')

    def test_unicode(self):
        o = Subspecies.objects.get(subspecies="LV")
        self.assertTrue(isinstance(o, Subspecies))
        self.assertEqual(o.__unicode__(), u'LV')


class SampleSubspeciesTest(TestCase):
    def setUp(self):
        o = Subspecies.objects.create(subspecies='LV')
        sub = SampleSubspecies.objects.create(subspecies_fk=o, sample_id=1)

    def test_unicode(self):
        sub = SampleSubspecies.objects.get(sample_id=1)
        self.assertTrue(isinstance(sub, SampleSubspecies))
        self.assertEqual(sub.__unicode__(), u'1')


class SamplesTest(TestCase):
    def setUp(self):
        o = Samples.objects.create(mip_fk=Mip.objects.create(mip_id=1, mip_start=1, mip_stop=2),
                                   sample_fk=SampleSubspecies.objects.create(
                                       subspecies_fk=Subspecies.objects.create(subspecies='LV'),
                                       sample_id=1))

    def test_unicode(self):
        o = Samples.objects.get(mip_fk=Mip.objects.get(mip_id=1, ), sample_fk=SampleSubspecies.objects.get(sample_id=1))
        self.assertTrue(isinstance(o, Samples))
        self.assertEquals(o.__unicode__(), u'mip|sample: 1|1')


class ParalogTest(TestCase):
    def setUp(self):
        o = Paralog.objects.create(mip_fk=Mip.objects.create(mip_id=1, mip_start=1, mip_stop=2),
                                   subspecies_fk=Subspecies.objects.create(subspecies='LV'),
                                   mip_subspecies_paralog='par')

    def test_unicode(self):
        o = Paralog.objects.get(mip_fk=Mip.objects.get(mip_id=1), subspecies_fk=Subspecies.objects.get(subspecies='LV'))
        self.assertTrue(isinstance(o, Paralog))
        self.assertEquals(o.__unicode__(), u'mip|subspecies|paralog: 1|LV|par')
