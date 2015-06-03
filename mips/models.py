""" Mip markers model. """

from django.db import models


class Mip(models.Model):
    """
    A class store info for Mip markers.
    """

    mip_id = models.IntegerField(null=False, unique=True, primary_key=True)
    mip_sequence = models.TextField()
    mip_extension_arm = models.TextField()
    mip_ligation_arm = models.TextField()
    mip_func_immuno = models.BooleanField(default=False)
    mip_func_mapping = models.BooleanField(default=False)
    mip_func_random = models.BooleanField(default=False)
    mip_func_utr = models.BooleanField(default=False)
    mip_start = models.IntegerField()
    mip_stop = models.IntegerField()
    reference_id = models.TextField(null=True)
    mip_comments = models.TextField(null=True)

    def __unicode__(self):
        return u'{}'.format(self.mip_id)


class Instance(models.Model):
    """
    A class for storing Mip instances of each used Mip.
    Designed Mip marker can be produced/bought many times
    and this allows to keep track of it

    Mip id, Mip pool & Mip instance makes a unique key
    """

    mip_fk = models.ForeignKey(Mip, null=False)
    mip_pool = models.IntegerField(null=False)
    mip_production_data = models.DateField()
    mip_producer = models.CharField(max_length=255)
    mip_plate = models.CharField(max_length=255)
    mip_position = models.CharField(max_length=50)
    mip_instance = models.IntegerField(null=False)

    def __unicode__(self):
        return u'mip|mip_instance: {}|{}'.format(self.mip_fk, self.mip_instance)


class Subspecies(models.Model):
    """
    A class to store taxonomic info.
    """

    subspecies = models.CharField(max_length=255, primary_key=True)

    def __unicode__(self):
        return u'{}'.format(self.subspecies)


class SampleSubspecies(models.Model):
    """
    A simple class to store taxonomic membership for each sample.
    """

    sample_id = models.IntegerField(primary_key=True)
    subspecies_fk = models.ForeignKey(Subspecies)

    def __unicode__(self):
        return u'{}'.format(self.sample_id)


class Samples(models.Model):
    """
    A class for storing Mip info for samples.

    Mip (id) & sample (id) makes a unique key
    """

    mip_fk = models.ForeignKey(Mip)
    sample_fk = models.ForeignKey(SampleSubspecies)

    mip_sequence = models.TextField()
    mip_performance = models.BooleanField(default=False)

    def __unicode__(self):
        return u'mip|sample: {}|{}'.format(self.mip_fk, self.sample_fk)


class Paralog(models.Model):
    """
    A class to store paralogy status of each marker within taxonomic group

    Mip (id) & subspecies (id) makes a unique key
    """

    mip_fk = models.ForeignKey(Mip)
    subspecies_fk = models.ForeignKey(Subspecies)
    mip_subspecies_paralog = models.CharField(max_length=50)

    def __unicode__(self):
        return u'mip|subspecies|paralog: {}|{}|{}'.format(self.mip_fk, self.subspecies_fk,
                                                          self.mip_subspecies_paralog)
