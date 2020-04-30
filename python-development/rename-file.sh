#!/bin/bash

DIR=$1
OLD_STRING=$2
NEW_STRING=$3

# One liner
find $DIR -type f -name "*$OLD_STRING*" | sed -e "p;s/$OLD_STRING/$NEW_STRING/g" | xargs -n2 mv

/*
for file in $(find $DIR -type f -name "*$OLD_STRING*"); do
    echo "Moving $file.."
    mv $file `echo $file | sed "s/$OLD_STRING/$NEW_STRING/g"`
done
*/
