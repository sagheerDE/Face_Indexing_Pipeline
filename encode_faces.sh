#!/bin/bash


source env/bin/activate
a=$(env/bin/python3 encode_faces.py $1)
echo $a
