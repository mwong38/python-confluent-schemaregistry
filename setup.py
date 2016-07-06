# Setup
try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup
from sys import version_info

import confluent.schemaregistry

if version_info >= (3,2):
    install_requires = ['avro-python3']
else:
    install_requires = ['avro']

version = '.'.join([ str(confluent.schemaregistry.__version__[i]) for i in range(3) ])

setup(
    name = 'confluent-schemaregistry',
    version = version,
    packages = ['confluent',
                'confluent.schemaregistry',
                'confluent.schemaregistry.serializers',
                'confluent.schemaregistry.client'],


    # Project uses simplejson, so ensure that it gets installed or upgraded
    # on the target machine
    install_requires = install_requires,

    # metadata for upload to PyPI
    author = 'Verisign',
    author_email = 'vsrtc-dev@verisign.com',
    description = 'Confluent Schema Registry lib',
    keywords = 'confluent schema registry schemaregistry',
    extras_require = {
        'fastavro': ['fastavro'],
    },
    test_requires = ['unittest2']
)
