from django.db import models


class Mip(models.Model):

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
        return str(self.mip_id)


class Instance(models.Model):

    id = models.AutoField(primary_key=True)

    mip_id_fk = models.ForeignKey(Mip)
    mip_pool = models.IntegerField()
    mip_production_data = models.DateField()
    mip_producer = models.CharField(max_length=255)
    mip_plate = models.CharField(max_length=255)
    mip_position = models.CharField(max_length=50)
    mip_instance = models.IntegerField()

    def __unicode__(self):
        return "mip|mip_instance: {}|{}".format(str(self.mip_fk), str(self.mip_instance))


class SampleSpecies(models.Model):

    sample_id = models.IntegerField(primary_key=True)
    subspecies = models.CharField(max_length=255)

    def __unicode__(self):
        return str(self.sample_id)


class Samples(models.Model):

    id = models.AutoField(primary_key=True)

    mip_id_fk = models.ForeignKey(Mip)
    sample_id_fk = models.ForeignKey(SampleSpecies)
    mip_sequence = models.TextField()
    mip_performance = models.BooleanField(default=False)

    def __unicode__(self):
        return "mip|sample: {}|{}".format(str(self.mip_fk), str(self.sample_id_fk))


class Paralog(models.Model):

    id = models.AutoField(primary_key=True)
    mip_id_fk = models.ForeignKey(Mip)

    # TODO: ???
    subspecies = models.CharField(max_length=100)
    mip_subspecies_paralog = models.CharField(max_length=50)

    def __unicode__(self):
        return "mip|subspecies|paralog: {}|{}|{}".format(str(self.mip_fk), str(self.subspecies),
                                                         self.mip_subspecies_paralog)
