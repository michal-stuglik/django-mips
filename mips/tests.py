from django.test import TestCase
from models import Mip


# Create your tests here.


# models test
class MipTestCase(TestCase):

    def setUp(self):
        o = Mip.objects.create(mip_id=1, mip_start=1, mip_stop=2)
        o.save()

    def test_mip_id_repr(self):
        mip1 = Mip.objects.get(mip_id=1)
        self.assertEqual(mip1.__unicode__(), u'1')