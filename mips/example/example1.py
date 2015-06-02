import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")

django.setup()


from mips.models import Mip, Subspecies, SampleSubspecies, Samples, Paralog, Instance


for mip in Mip.objects.all():
    print mip.mip_id