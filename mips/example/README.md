
# Example


More features & examples can be found in Django project site:
https://docs.djangoproject.com/en/1.8/ref/models/querysets/

## Requirements

To play with django without manage.py in plain python shell:

1. set the DJANGO_SETTINGS_MODULE environment variable to "mips.settings"
2. set up Django: django.setup()
    


```python
import os
import django

# set the DJANGO_SETTINGS_MODULE environment variable to "mips.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mips.settings")

# setup
django.setup()
```

## Import/update into database


## Select data from database


##### Select all Mip objects & print

```python
def select_all_mip_objects():

    for mip in Mip.objects.all():
        print mip
```
