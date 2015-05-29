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
    # id = models.AutoField(primary_key=True)

    mip_fk = models.ForeignKey(Mip, null=False)
    mip_pool = models.IntegerField(null=False)
    mip_production_data = models.DateField()
    mip_producer = models.CharField(max_length=255)
    mip_plate = models.CharField(max_length=255)
    mip_position = models.CharField(max_length=50)
    mip_instance = models.IntegerField(null=False)

    def __unicode__(self):
        return "mip|mip_instance: {}|{}".format(str(self.mip_fk), str(self.mip_instance))


class Subspecies(models.Model):
    subspecies = models.CharField(max_length=255, primary_key=True)

    def __unicode__(self):
        return self.subspecies


class SampleSubspecies(models.Model):
    sample_id = models.IntegerField(primary_key=True)
    subspecies_fk = models.ForeignKey(Subspecies)

    def __unicode__(self):
        return self.sample_id


class Samples(models.Model):
    id = models.AutoField(primary_key=True)

    mip_fk = models.ForeignKey(Mip)
    sample_fk = models.ForeignKey(SampleSubspecies)
    mip_sequence = models.TextField()
    mip_performance = models.BooleanField(default=False)

    def __unicode__(self):
        return "mip|sample: {}|{}".format(str(self.mip_fk), str(self.sample_fk))


class Paralog(models.Model):
    id = models.AutoField(primary_key=True)

    mip_fk = models.ForeignKey(Mip)
    subspecies_fk = models.ForeignKey(Subspecies)
    mip_subspecies_paralog = models.CharField(max_length=50)

    def __unicode__(self):
        return "mip|subspecies|paralog: {}|{}|{}".format(str(self.mip_fk), str(self.subspecies_fk),
                                                         self.mip_subspecies_paralog)
