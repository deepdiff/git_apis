#!/usr/bin/env python3
"""
Example of using GitHub GraphQL API via GitHub CLI.
"""

import subprocess
import json

def call_graphql_api(query, variables=None):
    """
    Call GitHub GraphQL API using gh CLI.
    
    Args:
        query: GraphQL query string
        variables: Optional variables dictionary
    
    Returns:
        JSON response from the API
    """
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    
    return json.loads(result.stdout) if result.stdout else None

def get_repository_info(owner, name):
    """Get repository information using GraphQL."""
    query = """
    query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) {
        name
        description
        stargazerCount
        forkCount
        createdAt
        updatedAt
      }
    }
    """
    variables = {"owner": owner, "name": name}
    return call_graphql_api(query, variables)

if __name__ == "__main__":
    print("GitHub GraphQL API Example")
    print("=" * 40)
    
    # Example: Get info about this repository
    print("\nGetting repository information...")
    # This would need to be customized with actual owner/repo
    print("GraphQL query example ready to use")

