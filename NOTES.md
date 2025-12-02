# GitHub API Learning Notes

## REST API Basics

- Base URL: `https://api.github.com`
- Authentication: Use `gh` CLI or personal access tokens
- Rate limits: 5000 requests/hour for authenticated users

## Common Endpoints

- `GET /user` - Current authenticated user
- `GET /user/repos` - User's repositories
- `GET /repos/:owner/:repo` - Repository information
- `GET /repos/:owner/:repo/commits` - Repository commits
- `GET /repos/:owner/:repo/issues` - Repository issues

## GraphQL API

- Endpoint: `https://api.github.com/graphql`
- Single endpoint for all queries
- More flexible than REST for complex queries

## Using GitHub CLI

```bash
# Get user info
gh api user

# Get repository info
gh api repos/owner/repo

# GraphQL query
gh api graphql -f query='{ viewer { login } }'
```

