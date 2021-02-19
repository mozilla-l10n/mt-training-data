#! /usr/bin/env bash

# Temporary fix for 1681653

script_path=$(dirname "$0")
root_path="${script_path}/../.."

for file in "${root_path}"/*/*.tmx
do
    if [ -f "${file}" ]
    then
        echo "Cleaning up: ${file}"
        sed -i "s/\x03//g" "${file}"
    else
        echo "No TMX file found"
    fi
done
