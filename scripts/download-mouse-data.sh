#!/bin/env bash

# File:   download-mouse-data.sh
# Date:   2024-12-04
# Author: Hank Feild
# Purpose: Downloads the files chr1.Build37.data -- chr20.Build37.data from
#          http://mtweb.cs.ucl.ac.uk/HSMICE/GENOTYPES


if [[ $# -lt 1 || "$1" == '-h' ]]; then 
    echo "USAGE: ./download-mouse-data.sh <dest directory> [--skip]"
    echo "Including --skip will cause files already downloaded to be skipped."
    exit
fi

destDir="$1"
skipExisting=0

# Check is user want's to skip existing files.
if [[ $# -gt 1 && "$2" == "--skip" ]]; then
    skipExisting=1
fi

# Ensure the destination directory exists and is a directory.
if [[ ! -d "$destDir" ]]; then
    echo "ERROR: $destDir is not a directory!"
    exit
fi

# Download all the files.
for i in {1..20}; do 
    filename="chr${i}.Build37.data"
    if [[ $skipExisting -eq 1 && -f "$destDir/$filename" ]]; then 
        echo "Skipping $filename (already downloaded)..."
    else
        echo "Downloading $filename..."
        curl -o "$destDir/$filename" http://mtweb.cs.ucl.ac.uk/HSMICE/GENOTYPES/$filename
        sleep .5
    fi
done