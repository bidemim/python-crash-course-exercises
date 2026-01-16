#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status,
# treat unset variables as an error and fail pipelines on the first failing command.
set -euo pipefail

# Enable bash nullglob so globs that don't match expand to an empty list
# (prevents literal patterns from being used as filenames).
shopt -s nullglob

# Create 20 chapter folders named Chapter_1 .. Chapter_20
for i in {1..20}; do
  # Use -p to avoid error if the directory already exists
  mkdir -p "Chapter_${i}"
done

# For each numeric prefix (1..20), move files that start with "<N>-"
# into the corresponding Chapter_N directory.
for p in {1..20}; do
  # Expand files that start with the prefix and a dash (e.g. "1-abc.txt")
  files=( "${p}-"* )

  # If the array length is greater than zero, move the files
  if [ "${#files[@]}" -gt 0 ]; then
    # Use -- to protect filenames that start with a dash
    mv -- "${files[@]}" "Chapter_${p}/"
  fi
done

# Disable nullglob to restore shell state
shopt -u nullglob

# Print a summary message
echo "Moved files by prefix into Chapter_1..Chapter_20"
