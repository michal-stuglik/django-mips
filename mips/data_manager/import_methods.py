"""
Modules with functions for manipulating data in database
"""

import os
from datetime import date
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")
import django

django.setup()

from mips.models import Mip, Subspecies, SampleSubspecies, Samples, Paralog, Instance

# TODO: get table schema from database!
mip_table_input_schema = ["MIP_ID", "MIP_sequence", "MIP_extension_arm", "MIP_ligation_arm", "MIP_function_immuno",
                          "MIP_function_mapping", "MIP_function_random", "MIP_function_UTR", "Reference_ID",
                          "MIP_start",
                          "MIP_stop",
                          "Comments"
                          ]

subspecies_input_schema = ["Subspecies"]

sample_subspecies_input_schema = ['Sample_ID', 'Subspecies']

samples_input_schema = ['MIP_ID', 'Sample_ID', 'Sample_MIP_sequence', 'Sample_MIP_performance']

paralogs_input_schema = ['MIP_ID', 'Subspecies', 'Subspecies_MIP_paralog']

instance_input_schema = ['MIP_ID', 'MIP_pool', 'MIP_production_date', 'MIP_producer', 'MIP_plate', 'MIP_position',
                         'MIP_instance']


def final_print(method_name, obj_row_counter, table_row_counter, saved_row_counter):
    """Final method print. """

    print 'Function {} objects/imported/updated: {}/{}/{} rows into database'.format(method_name, obj_row_counter,
                                                                                     saved_row_counter,
                                                                                     table_row_counter)


def load_mips(file_path):
    """Insert/Update mip objects. """

    print 'Function {} ...'.format(load_mips.__name__)

    header_read = False
    with open(file_path, 'r') as f:

        table_row_counter = 0
        saved_row_counter = 0
        obj_row_counter = 0

        for line in f:

            row_as_list = line.rstrip('\r\n').split('\t')

            if not header_read:
                if cmp(row_as_list, mip_table_input_schema) != 0:
                    raise Exception(
                        "Mixed field names/order between tables:\nDefined table:{}\nImported table:{}".format(
                            mip_table_input_schema,
                            row_as_list))
                header_read = True
                continue

            # all data rows counter
            table_row_counter += 1

            mip_id = row_as_list[0]
            mip_sequence = row_as_list[1]
            mip_extension_arm = row_as_list[2]
            mip_ligation_arm = row_as_list[3]
            mip_function_immuno = row_as_list[4]
            mip_function_mapping = row_as_list[5]
            mip_function_random = row_as_list[6]
            mip_function_utr = row_as_list[7]
            reference_id = row_as_list[8]

            mip_start = row_as_list[9]
            mip_stop = row_as_list[10]
            mip_comments = str(row_as_list[11]).strip()

            # database writer
            obj, created = Mip.objects.update_or_create(mip_id=mip_id, defaults={'mip_sequence': mip_sequence,
                                                                                 'mip_extension_arm': mip_extension_arm,
                                                                                 'mip_ligation_arm': mip_ligation_arm,
                                                                                 'mip_func_immuno': mip_function_immuno,
                                                                                 'mip_func_mapping': mip_function_mapping,
                                                                                 'mip_func_random': mip_function_random,
                                                                                 'mip_func_utr': mip_function_utr,
                                                                                 'reference_id': reference_id,
                                                                                 'mip_start': mip_start,
                                                                                 'mip_stop': mip_stop,
                                                                                 'mip_comments': mip_comments}
                                                        )

            if obj:
                obj_row_counter += 1

            if created:
                saved_row_counter += 1

            if table_row_counter % 100 == 0:
                print 'Importing paralogs #: {}'.format(table_row_counter)

    final_print(sys._getframe().f_code.co_name, obj_row_counter, table_row_counter, saved_row_counter)


def load_subspecies(file_path):
    print 'Function {} ...'.format(load_subspecies.__name__)

    header_read = False
    with open(file_path, 'r') as f:

        table_row_counter = 0
        saved_row_counter = 0
        obj_row_counter = 0

        for line in f:

            row_as_list = line.rstrip('\r\n').split('\t')

            if not header_read:
                if cmp(row_as_list, subspecies_input_schema) != 0:
                    raise Exception(
                        "Mixed field names/order between tables:\nDefined table:{}\nImported table:{}".format(
                            subspecies_input_schema,
                            row_as_list))
                header_read = True
                continue

            # all data rows counter
            table_row_counter += 1

            subspecies = row_as_list[0]

            # database writer
            obj, created = Subspecies.objects.update_or_create(subspecies=subspecies)

            if obj:
                obj_row_counter += 1

            if created:
                saved_row_counter += 1

            if table_row_counter % 100 == 0:
                print 'Importing paralogs #: {}'.format(table_row_counter)

    final_print(sys._getframe().f_code.co_name, obj_row_counter, table_row_counter, saved_row_counter)


def load_sample_subspecies(file_path):
    print 'Function {} ...'.format(load_sample_subspecies.__name__)

    header_read = False
    with open(file_path, 'r') as f:

        table_row_counter = 0
        saved_row_counter = 0
        obj_row_counter = 0

        for line in f:

            row_as_list = line.rstrip('\r\n').split('\t')

            if not header_read:
                if cmp(row_as_list, sample_subspecies_input_schema) != 0:
                    raise Exception(
                        "Mixed field names/order between tables:\nDefined table:{}\nImported table:{}".format(
                            sample_subspecies_input_schema,
                            row_as_list))
                header_read = True
                continue

            # all data rows counter
            table_row_counter += 1

            sample_id = row_as_list[0]
            subspecies_txt = row_as_list[1]

            # database writer
            subspecies = Subspecies.objects.get(subspecies=subspecies_txt)
            obj, created = SampleSubspecies.objects.update_or_create(sample_id=sample_id,
                                                                     defaults={'subspecies_fk': subspecies})
            if obj:
                obj_row_counter += 1

            if created:
                saved_row_counter += 1

            if table_row_counter % 100 == 0:
                print 'Importing paralogs #: {}'.format(table_row_counter)

    final_print(sys._getframe().f_code.co_name, obj_row_counter, table_row_counter, saved_row_counter)


def load_samples(file_path):
    print 'Function {} ...'.format(load_samples.__name__)

    header_read = False
    with open(file_path, 'r') as f:

        table_row_counter = 0
        saved_row_counter = 0
        obj_row_counter = 0

        for line in f:

            row_as_list = line.rstrip('\r\n').split('\t')

            if not header_read:
                if cmp(row_as_list, samples_input_schema) != 0:
                    raise Exception(
                        "Mixed field names/order between tables:\nDefined table:{}\nImported table:{}".format(
                            samples_input_schema,
                            row_as_list))
                header_read = True
                continue

            # all data rows counter
            table_row_counter += 1

            mip_id_txt = row_as_list[0]
            sample_id_txt = row_as_list[1]
            sample_mip_seq = row_as_list[2]
            sample_mip_performance = row_as_list[3]

            # database writer
            mip = Mip.objects.get(mip_id=mip_id_txt)
            sample = SampleSubspecies.objects.get(sample_id=sample_id_txt)

            # mip & sample - a unique key
            obj, created = Samples.objects.update_or_create(mip_fk=mip, sample_fk=sample,
                                                            defaults={'mip_sequence': sample_mip_seq,
                                                                      'mip_performance': sample_mip_performance})

            if obj:
                obj_row_counter += 1

            if created:
                saved_row_counter += 1

            if table_row_counter % 100 == 0:
                print 'Importing paralogs #: {}'.format(table_row_counter)

    final_print(sys._getframe().f_code.co_name, obj_row_counter, table_row_counter, saved_row_counter)


def load_paralogs(file_path):
    print 'Function {} ...'.format(load_paralogs.__name__)

    header_read = False
    with open(file_path, 'r') as f:

        table_row_counter = 0
        saved_row_counter = 0
        obj_row_counter = 0

        for line in f:

            row_as_list = line.rstrip('\r\n').split('\t')

            if not header_read:
                if cmp(row_as_list, paralogs_input_schema) != 0:
                    raise Exception(
                        "Mixed field names/order between tables:\nDefined table:{}\nImported table:{}".format(
                            paralogs_input_schema,
                            row_as_list))
                header_read = True
                continue

            # all data rows counter
            table_row_counter += 1

            mip_id_txt = row_as_list[0]
            subspecies_txt = row_as_list[1]
            mip_subspecies_paralog_txt = row_as_list[2]

            # mip & subspecies - a unique key
            mip = Mip.objects.get(mip_id=mip_id_txt)
            subspecies = Subspecies.objects.get(subspecies=subspecies_txt)

            obj, created = Paralog.objects.update_or_create(mip_fk=mip, subspecies_fk=subspecies,
                                                            defaults={
                                                                'mip_subspecies_paralog': mip_subspecies_paralog_txt})
            if obj:
                obj_row_counter += 1

            if created:
                saved_row_counter += 1

            if table_row_counter % 100 == 0:
                print 'Importing paralogs #: {}'.format(table_row_counter)

    final_print(sys._getframe().f_code.co_name, obj_row_counter, table_row_counter, saved_row_counter)


def load_mip_instances(file_path):
    print 'Function {} ...'.format(load_mip_instances.__name__)

    header_read = False
    with open(file_path, 'r') as f:

        table_row_counter = 0
        saved_row_counter = 0
        obj_row_counter = 0

        for line in f:

            row_as_list = line.rstrip('\r\n').split('\t')

            if not header_read:
                if cmp(row_as_list, instance_input_schema) != 0:
                    raise Exception(
                        "Mixed field names/order between tables:\nDefined table:{}\nImported table:{}".format(
                            instance_input_schema,
                            row_as_list))
                header_read = True
                continue

            # all data rows counter
            table_row_counter += 1

            mip_id_txt = row_as_list[0]
            mip_pool_txt = row_as_list[1]
            mip_production_data_txt = date(int(str(row_as_list[2]).split("-")[2]),
                                           int(str(row_as_list[2]).split("-")[1]),
                                           int(str(row_as_list[2]).split("-")[0]))

            mip_producer_txt = row_as_list[3]
            mip_plate_txt = row_as_list[4]
            mip_position_txt = row_as_list[5]
            mip_instance_txt = row_as_list[6]

            mip = Mip.objects.get(mip_id=mip_id_txt)

            # database writer
            obj, created = Instance.objects.update_or_create(mip_fk=mip, mip_pool=mip_pool_txt,
                                                             mip_instance=mip_instance_txt,
                                                             defaults={'mip_production_data': mip_production_data_txt,
                                                                       'mip_producer': mip_producer_txt,
                                                                       'mip_plate': mip_plate_txt,
                                                                       'mip_position': mip_position_txt})
            if obj:
                obj_row_counter += 1

            if created:
                saved_row_counter += 1

            if table_row_counter % 100 == 0:
                print 'Importing paralogs #: {}'.format(table_row_counter)

    final_print(sys._getframe().f_code.co_name, obj_row_counter, table_row_counter, saved_row_counter)
