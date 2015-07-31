from django.test import TestCase
from models import Mip

# Create your tests here.


# models test
class MipTest(TestCase):

    def create_mip(self, mip_id=1):
        return Mip.objects.create(mip_id=mip_id)

    def test_mip_creation(self):
        w = self.create_mip()
        self.assertTrue(isinstance(w, Mip))
        self.assertEqual(w.__unicode__(), w.title)


