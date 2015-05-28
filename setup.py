import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mips',
    version='0.1.0',
    packages=['mips'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to store and process mip data.',
    long_description=README,
    url='https://github.com/michal-stuglik/django-mips',
    author='Michal Stuglik',
    author_email='michal@codelabs.info',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
) 
