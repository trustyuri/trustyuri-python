#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd ../src && pwd )"
python $DIR/hashuri/rdf/TransformRdf.py $*
