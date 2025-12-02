#!/bin/bash
echo "=== GitHub Authentication Status ==="
gh auth status

echo ""
echo "=== Current User ==="
gh api user | jq -r '.login, .name, .email' || gh api user

echo ""
echo "=== Git Status ==="
git status 2>&1 || echo "Not a git repository"

echo ""
echo "=== Git Remote ==="
git remote -v 2>&1 || echo "No remotes configured"

echo ""
echo "=== Repository Check ==="
gh repo list --limit 10 || echo "Could not list repositories"

