#!/bin/sh
count=0

for fileSource in *.svg
do
    if [ -f "$fileSource" ]; then    
        count=$((count+1))
        file=$(echo $fileSource | cut -d'.' -f1)
        echo $count". "$fileSource" -> "$file.eps
        inkscape $fileSource --export-eps=../eps/$file.eps --export-ignore-filters --export-ps-level=3
    else
        echo "no file $fileSource found!"
    fi
done
echo "$count file(s) converted!"
