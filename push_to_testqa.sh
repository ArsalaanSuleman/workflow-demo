#!/bin/bash
# Automate pushing changes from dev to testqa

# Check out dev branch
git checkout dev

# Pull latest changes
git pull origin dev

# Push changes to testqa
git push origin dev:testqa

echo "Changes from dev have been pushed to testqa."

# ./push_to_testqa.sh
