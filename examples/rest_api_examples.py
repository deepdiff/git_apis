#!/usr/bin/env python3
"""
Examples of various GitHub REST API endpoints.
"""

import subprocess
import json

def call_api(endpoint, method="GET"):
    """Call GitHub REST API endpoint."""
    result = subprocess.run(
        ["gh", "api", endpoint, "-X", method],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    
    return json.loads(result.stdout) if result.stdout else None

def list_issues(owner, repo, state="open"):
    """List issues for a repository."""
    endpoint = f"repos/{owner}/{repo}/issues?state={state}"
    return call_api(endpoint)

def get_repository(owner, repo):
    """Get repository information."""
    endpoint = f"repos/{owner}/{repo}"
    return call_api(endpoint)

def list_commits(owner, repo, branch="main"):
    """List commits for a repository."""
    endpoint = f"repos/{owner}/{repo}/commits?sha={branch}"
    return call_api(endpoint)

if __name__ == "__main__":
    print("GitHub REST API Examples")
    print("=" * 40)
    print("Various REST API endpoint examples")
    print("Ready to use with your repository!")

