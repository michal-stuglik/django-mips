# import sys
import os

from mips.data_manager import import_methods

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    #
    import_methods.load_mips(os.path.join(BASE_DIR, "data_manager/sample_data/MIP.txt"))
    #
    import_methods.load_subspecies(os.path.join(BASE_DIR, "data_manager/sample_data/Subspecies.txt"))

    import_methods.load_sample_subspecies(os.path.join(BASE_DIR, "data_manager/sample_data/SampleSubspecies.txt"))

    # MIP_sample data
    import_methods.load_samples(os.path.join(BASE_DIR, "data_manager/sample_data/MIP_samples.txt"))

    # MIP_paralogs data
    import_methods.load_paralogs(os.path.join(BASE_DIR, "data_manager/sample_data/MIP_paralogs.txt"))

    # MIP_instance data
    import_methods.load_mip_instances(os.path.join(BASE_DIR, "data_manager/sample_data/MIP_instance.txt"))

except:
    raise

