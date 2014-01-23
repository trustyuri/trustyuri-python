hashuri-python
==============

This code generates and checks URIs that represent content such as plain bytes or RDF data, and
contain a cryptographic hash value. This hash can be used to check that the respective content has
not been accidentally or deliberately modified. This is an examle of a hash-URI:

> http://example.org/np1.RAcbjcRIQozo2wBMq4WcCYkFAjRz0AX-Ux3PquZZrC68s

See the [hash-URI specification](https://github.com/tkuhn/hashuri-spec) and the
[preprint article](http://arxiv.org/abs/1401.5775) describing the approach.


Dependencies
------------

You have to install the rdflib package:

    $ pip install rdflib


License
-------

hashuri-python is free software under the MIT License. See LICENSE.txt.
