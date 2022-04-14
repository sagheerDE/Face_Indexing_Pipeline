#!/bin/bash


source env/bin/activate
a=$(env/bin/python3 post_face_api.py $1)
echo $a
