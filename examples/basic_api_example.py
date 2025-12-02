#!/usr/bin/env python3
"""
Basic example of using GitHub API via GitHub CLI or direct API calls.
This is a starting point for experimenting with GitHub APIs.
"""

import subprocess
import json
import os

def call_gh_api(endpoint, method="GET", data=None):
    """
    Call GitHub API using gh CLI.
    
    Args:
        endpoint: API endpoint (e.g., 'user', 'repos')
        method: HTTP method (GET, POST, etc.)
        data: Optional data for POST/PATCH requests
    
    Returns:
        JSON response from the API
    """
    cmd = ["gh", "api", endpoint]
    
    if method != "GET":
        cmd.extend(["-X", method])
    
    if data:
        cmd.extend(["--input", "-"])
        result = subprocess.run(
            cmd,
            input=json.dumps(data).encode(),
            capture_output=True,
            text=True
        )
    else:
        result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    
    return json.loads(result.stdout) if result.stdout else None

def get_current_user():
    """Get information about the authenticated user."""
    return call_gh_api("user")

def list_repos(username=None):
    """List repositories for a user."""
    endpoint = f"users/{username}/repos" if username else "user/repos"
    return call_gh_api(endpoint)

def get_repo_info(owner, repo):
    """Get information about a specific repository."""
    endpoint = f"repos/{owner}/{repo}"
    return call_gh_api(endpoint)

def list_branches(owner, repo):
    """List branches for a repository."""
    endpoint = f"repos/{owner}/{repo}/branches"
    return call_gh_api(endpoint)

if __name__ == "__main__":
    print("GitHub API Experiment - Basic Example")
    print("=" * 40)
    
    # Get current user info
    print("\n1. Getting current user information...")
    user = get_current_user()
    if user:
        print(f"   Username: {user.get('login')}")
        print(f"   Name: {user.get('name', 'N/A')}")
        print(f"   Public Repos: {user.get('public_repos', 0)}")
    
    # List repositories
    print("\n2. Listing repositories...")
    repos = list_repos()
    if repos:
        print(f"   Found {len(repos)} repositories")
        if repos:
            print(f"   First repo: {repos[0].get('name')}")

