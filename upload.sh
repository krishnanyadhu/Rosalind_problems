#!/bin/bash

# Script to upload new/unuploaded files to GitHub
# Commit message = today's date

# Get today's date in YYYY-MM-DD format
COMMIT_MSG=$(date +"%Y-%m-%d")

# Stage all new and modified files
git add .

# Commit with today's date
git commit -m "$COMMIT_MSG"

# Push to GitHub main branch
git push origin main
