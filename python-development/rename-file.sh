#!/bin/bash

DIR=$1
OLD_STRING=$2
NEW_STRING=$3

for file in $(find $DIR -type f -name "*$OLD_STRING*"); do
    echo "Moving $file.."
    mv $file `echo $file | sed "s/$OLD_STRING/$NEW_STRING/g"`
done

