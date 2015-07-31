from django.test import TestCase
from models import Mip

# Create your tests here.


# models test
class MipTestCase(TestCase):
    def setUp(self):
        Mip.objects.create(mip_id=1)

    def test_mip_id(self):
        mip1 = Mip.objects.get(mip_id=1)
        self.assertEqual(mip1.__unicode__(), u'1')

    #
    # def create_mip(self, mip_id=1):
    #     return Mip.objects.create(mip_id=mip_id)
    #
    # def test_mip_creation(self):
    #     w = self.create_mip()
    #     self.assertTrue(isinstance(w, Mip))
    #     self.assertEqual(w.__unicode__(), w.title)
    #

