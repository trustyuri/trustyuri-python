hashuri-python
==============

This code generates and checks URIs that represent content such as plain bytes or RDF data, and
contain a cryptographic hash value. This hash can be used to check that the respective content has
not been accidentally or deliberately modified. This is an examle of a hash-URI:

> http://example.org/np1.RAcbjcRIQozo2wBMq4WcCYkFAjRz0AX-Ux3PquZZrC68s

See the hash-URI specification (work in progress): https://github.com/tkuhn/hashuri-spec


Dependencies
------------

You have to install the rdflib package:

    $ pip install rdflib


License
-------

hashuri-python is free software under the MIT License. See LICENSE.txt.
