#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd ../ && pwd )"
export PYTHONPATH=$PYTHONPATH:$DIR
python $DIR/trustyuri/rdf/TransformRdf.py $*
