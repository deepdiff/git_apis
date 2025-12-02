#!/bin/bash
set -e

echo "=== Current Status ==="
git status --short

echo ""
echo "=== Making commits ==="

# Commit 1: GraphQL example
git add examples/graphql_example.py
git commit -m "Add GraphQL API example script" || echo "Commit 1 failed or nothing to commit"

# Commit 2: Update README
git add README.md
git commit -m "Update README with examples section" || echo "Commit 2 failed or nothing to commit"

# Commit 3: REST API examples
git add examples/rest_api_examples.py
git commit -m "Add REST API examples module" || echo "Commit 3 failed or nothing to commit"

# Commit 4: Update basic example
git add examples/basic_api_example.py
git commit -m "Add more helper functions to basic API example" || echo "Commit 4 failed or nothing to commit"

# Commit 5: Requirements
git add requirements.txt
git commit -m "Add requirements.txt file" || echo "Commit 5 failed or nothing to commit"

# Commit 6: Notes
git add NOTES.md
git commit -m "Add learning notes document" || echo "Commit 6 failed or nothing to commit"

echo ""
echo "=== Final Status ==="
git status --short

echo ""
echo "=== Commit History ==="
git log --oneline -10

