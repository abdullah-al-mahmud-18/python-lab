#!/bin/bash

file="$1"

if [[ -z "$file" ]]; then
    echo "Error: file name required"
    exit 1
fi

file_path=$(find . -type f -name "$file" -print -quit)

echo "Executing $file_path"

uv run "$file_path" test run

