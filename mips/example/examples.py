""" Module with example methods to select and modify objects in MIP database.

    To play with django without manage.py in plain pyyhon shell
    1. set the DJANGO_SETTINGS_MODULE environment variable to "mips.settings"
    2. set up Django: django.setup()
"""

import os
import django

# set the DJANGO_SETTINGS_MODULE environment variable to "mips.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")

# setup
django.setup()

# import proper classes to play with
from mips.models import Mip, Subspecies, SampleSubspecies, Samples, Paralog, Instance


def select_all_mip_objects():
    """Select all Mip objects & print. """

    for mip in Mip.objects.all():
        print mip


def select_mips_from_reference_seq(reference_name):
    """Select all Mip objects located on specific reference sequence. """

    for mip in Mip.objects.filter(reference_id=reference_name):
        print mip





# select_all_mip_objects()

# select_mips_from_reference_seq("c132510_g1_i1")
