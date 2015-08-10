import os
import django
import datetime

# set the DJANGO_SETTINGS_MODULE environment variable to "mips.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")

# setup
django.setup()

from django.test import TestCase
from model_mommy import mommy
from models import Mip, Instance, Subspecies, SampleSubspecies, Samples, Paralog


# class MipTest(TestCase):
#     def setUp(self):
#         o = Mip.objects.create(mip_id=1, mip_start=1, mip_stop=2)
#
#     def test_unicode(self):
#         mip1 = Mip.objects.get(mip_id=1)
#         self.assertTrue(isinstance(mip1, Mip))
#         self.assertEqual(mip1.__unicode__(), u'1')


class MipTestMommy(TestCase):
    def setUp(self):
        self.o = mommy.make(Mip)

    def tearDown(self):
        self.o.delete()

    def test_unicode(self):
        # mip1 = mommy.make(Mip)
        self.assertTrue(isinstance(self.o, Mip))
        self.assertEqual(self.o.__unicode__(), u'%s' % self.o.mip_id)


class InstanceTestMommy(TestCase):
    def setUp(self):
        self.o = mommy.make(Instance)

    def tearDown(self):
        self.o.delete()

    def test_unicode(self):
        # o = mommy.make(Instance)
        self.assertTrue(isinstance(self.o, Instance))
        self.assertEqual(self.o.__unicode__(),
                         u'mip|mip_instance: {}|{}'.format(self.o.mip_fk.mip_id, self.o.mip_instance))


class SubspeciesTestMommy(TestCase):
    def setUp(self):
        self.o = mommy.make(Subspecies)

    def tearDown(self):
        self.o.delete()

    def test_unicode(self):
        # o = mommy.make(Subspecies)
        self.assertTrue(isinstance(self.o, Subspecies))
        self.assertEqual(self.o.__unicode__(), u'{}'.format(self.o.subspecies))


class SampleSubspeciesMommy(TestCase):
    def setUp(self):
        self.o = mommy.make(SampleSubspecies)

    def tearDown(self):
        self.o.delete()

    def test_unicode(self):
        self.assertTrue(isinstance(self.o, SampleSubspecies))
        self.assertEqual(self.o.__unicode__(), u'{}'.format(self.o.sample_id))


class SamplesTest(TestCase):
    def setUp(self):
        self.o = mommy.make(Samples)

    def tearDown(self):
        self.o.delete()

    def test_unicode(self):
        self.assertTrue(isinstance(self.o, Samples))
        self.assertEquals(self.o.__unicode__(),
                          u'mip|sample: {}|{}'.format(self.o.mip_fk.mip_id, self.o.sample_fk.sample_id))


class ParalogTestMommy(TestCase):
    def setUp(self):
        self.o = mommy.make(Paralog)

    def tearDown(self):
        self.o.delete()

    def test_unicode(self):
        self.assertTrue(isinstance(self.o, Paralog))
        self.assertEquals(self.o.__unicode__(),
                          u'mip|subspecies|paralog: {}|{}|{}'.format(self.o.mip_fk.mip_id,
                                                                     self.o.subspecies_fk.subspecies,
                                                                     self.o.mip_subspecies_paralog))
