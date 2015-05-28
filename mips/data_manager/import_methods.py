"""
Modules with functions for manipulating data in database
"""


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")

from mips.models import Mip

# TODO: get table schema from database!
mip_table_schema = ["MIP_ID", "MIP_sequence", "MIP_extension_arm", "MIP_ligation_arm", "MIP_function_immuno",
             "MIP_function_mapping", "MIP_function_random", "MIP_function_UTR", "Reference_ID", "MIP_start", "MIP_stop",
             "Comments"
             ]


def mip_insert_update(file_path):
    """Insert/Update mip objects. """

    print 'Function {} ...'.format(mip_insert_update.__name__)

    header_read = False
    with open(file_path, 'r') as f:

        table_row_counter = 0
        saved_row_counter = 0

        for line in f:

            row_as_list = line.rstrip('\n').split('\t')

            if not header_read:
                if cmp(row_as_list, mip_table_schema) != 0:
                    raise Exception(
                        "Mixed field names/order between tables:\nDefined table:{}\nImported table:{}".format(mip_table_schema,
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
            mip = Mip(mip_id=mip_id, mip_sequence=mip_sequence, mip_extension_arm=mip_extension_arm,
                      mip_ligation_arm=mip_ligation_arm, mip_func_immuno=mip_function_immuno,
                      mip_func_mapping=mip_function_mapping, mip_func_random=mip_function_random,
                      mip_func_utr=mip_function_utr, reference_id=reference_id,
                      mip_start=mip_start, mip_stop=mip_stop, mip_comments=mip_comments
                      )

            # TODO: uniqe safe entry???

            mip.save()
            saved_row_counter += 1

            if table_row_counter % 100 == 0:
                print 'Importing mips #: {}'.format(table_row_counter)

    print 'Function {} imported {} into database'.format(mip_insert_update.__name__, table_row_counter)
