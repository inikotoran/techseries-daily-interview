#!/bin/bash
#

ID=`date +%y%m%d`
FILE_NAME="${ID}-$1.py"

touch $FILE_NAME

echo "$FILE_NAME created:"
