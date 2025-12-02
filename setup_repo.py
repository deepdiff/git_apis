#!/usr/bin/env python3
"""Script to check GitHub authentication and set up repository."""
import subprocess
import json
import sys
import os

def run_cmd(cmd, capture_output=True):
    """Run a command and return the result."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=capture_output,
            text=True,
            check=False
        )
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1

def main():
    print("=== Checking GitHub Authentication ===")
    stdout, stderr, code = run_cmd("gh auth status")
    print(stdout)
    if stderr:
        print("STDERR:", stderr)
    
    print("\n=== Getting Current User ===")
    stdout, stderr, code = run_cmd("gh api user")
    if stdout:
        try:
            user = json.loads(stdout)
            print(f"Logged in as: {user.get('login', 'Unknown')}")
            print(f"Name: {user.get('name', 'N/A')}")
            print(f"Email: {user.get('email', 'N/A')}")
        except:
            print(stdout)
    if stderr:
        print("STDERR:", stderr)
    
    print("\n=== Checking Git Status ===")
    stdout, stderr, code = run_cmd("git status")
    print(stdout)
    if stderr and "not a git repository" in stderr.lower():
        print("Initializing git repository...")
        run_cmd("git init")
        run_cmd("git add .")
        run_cmd('git commit -m "Initial commit"')
    
    print("\n=== Checking Remotes ===")
    stdout, stderr, code = run_cmd("git remote -v")
    print(stdout if stdout else "No remotes configured")
    
    print("\n=== Listing Repositories ===")
    stdout, stderr, code = run_cmd("gh repo list --limit 5")
    print(stdout)
    if stderr:
        print("STDERR:", stderr)

if __name__ == "__main__":
    main()

