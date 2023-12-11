#!/bin/bash

# Fetch updates from origin
git fetch origin --quiet

# Store the list of changed files
changed_files=$(git diff --name-only --diff-filter=ACMT origin/main...HEAD -- scenarios/ | grep -o 'scenarios/.*')

# Check if there are changed files
if [ -z "$changed_files" ]; then
    echo "No changes in scenarios/"
else
    # Run tests on changed files
    vedro run $changed_files
fi
