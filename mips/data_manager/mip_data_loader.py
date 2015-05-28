
import sys


from mips.data_manager import import_methods

# try:

    # con = lite.connect(DB)
    # cur = con.cursor()

import_methods.mip_insert_update("/home/michal/Dropbox/share_work/molecol/Newts_database/baza_MIPow/MIP.txt")

    # print "data loaded!"

# except Exception as e:
#
#     print "Error: {}".format(e)
#     # sys.exit(1)
#
# finally:
#     pass
#
