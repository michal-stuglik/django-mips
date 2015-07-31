#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    import django
    django.setup()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
