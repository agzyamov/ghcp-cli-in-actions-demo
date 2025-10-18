# GitHub Copilot CLI in Actions Demo

> Automate your software development lifecycle with GitHub Copilot CLI and Coding Agent in GitHub Actions

[![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-blue?logo=github-actions)](https://github.com/features/actions)
[![Copilot](https://img.shields.io/badge/GitHub-Copilot-purple?logo=github)](https://github.com/features/copilot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Overview

This repository demonstrates how to integrate GitHub Copilot CLI and GitHub Copilot Coding Agent into GitHub Actions workflows. Ask technical questions, get AI-powered answers automatically saved to a dedicated branch, or let the Copilot Agent autonomously create code for you with comprehensive security features to protect your repository.

## ✨ Features

- 📝 **Interactive Q&A**: Ask questions and get answers saved to a dedicated branch  
- 🤖 **Autonomous Coding Agent**: Let Copilot Agent create code and pull requests autonomously
- 🔒 **Security First**: Comprehensive security configuration with Dependabot, CODEOWNERS, and secret scanning
- 🎯 **Zero Configuration**: Works out of the box with GitHub Actions
- 🛡️ **Protected Main Branch**: Branch protection rules enforce code review workflow

## 📋 Prerequisites

- GitHub repository with Actions enabled
- GitHub Copilot subscription
- For Q&A: Personal Access Token (PAT) with Copilot scope
- For Coding Agent: OAuth token with appropriate permissions

## 🛠️ Setup

### For Contributors: Try It Yourself

Want to experiment with this demo? Fork the repository:

1. Click the **Fork** button at the top of this page
2. In your fork, go to `Settings` → `Actions` → `General` → Enable "Read and write permissions"
3. Create your own `COPILOT_TOKEN` secret (requires GitHub Copilot subscription)
4. Run the workflow: `gh workflow run copilot-qa.yml -f question="Your question here"`

Your fork will work independently with your own Copilot access and responses.

### For Repository Owners: Initial Setup

### 1. Configure Repository Settings

1. Go to `Settings` → `Actions` → `General`
2. Under **Workflow permissions**, select:
   - ✅ **Read and write permissions**

> **Note**: The workflow commits to the `copilot-responses` branch, which is not protected, so PR creation permissions are not required.

### 2. Add Secrets (Repository Owner Only)

#### For Copilot Q&A (`COPILOT_TOKEN`)

**Important**: GitHub Copilot CLI requires a regular GitHub Personal Access Token (PAT) with the `copilot` scope - it does NOT require a separate Copilot-specific token. The PAT allows the CLI to access GitHub Copilot on behalf of your account.

**Prerequisites:**
- Active GitHub Copilot subscription for your GitHub account
- Eligible plans: **Copilot Free**, **Copilot Pro**, **Copilot Pro+**, **Copilot Business**, or **Copilot Enterprise**
- For Free/Pro plans: [Sign up here](https://github.com/features/copilot)
- For organizations: Must be assigned Copilot access by your organization admin

**Setup steps:**

1. Create a [Personal Access Token (classic)](https://github.com/settings/tokens/new) with these scopes:
   - `repo` (Full control of private repositories) - *required for repository access*
   - `copilot` (GitHub Copilot) - **required to use Copilot API**

2. Add the token to repository secrets as `COPILOT_TOKEN`:
   ```
   Settings → Secrets and variables → Actions → New repository secret
   Name: COPILOT_TOKEN
   Value: <your-PAT-token>
   ```

#### For Copilot Coding Agent (`COPILOT_OAUTH_TOKEN`)

**Important**: GitHub Copilot Coding Agent requires a **Personal OAuth Token** generated through GitHub CLI authentication flow. This is different from a Personal Access Token (PAT).

**Prerequisites:**
- GitHub Copilot Business or Enterprise subscription
- Organization must have Copilot Agent features enabled
- GitHub CLI installed locally to generate the token

**⚠️ Token Types Explained:**

| Token Type | For Copilot CLI (Q&A) | For Copilot Agent | How to Get |
|------------|----------------------|-------------------|------------|
| **Personal Access Token (Classic)** | ✅ **YES** | ❌ **NO** | github.com/settings/tokens |
| **Personal OAuth Token** | ❌ **NO** | ✅ **YES** | `gh auth login` command |
| **Fine-grained PAT** | ✅ Maybe | ❌ **NO** | github.com/settings/tokens |
| **OAuth App Token** | ❌ **NO** | ❌ **NO** | N/A |
| **GitHub App Token** | ❌ **NO** | ❌ **NO** | N/A |

**Setup: Personal OAuth Token (Required for Agent)**

**Use:** Required for GitHub Copilot Agent workflow

1. **Generate Personal OAuth Token locally** using GitHub CLI:
   ```bash
   # Login to GitHub CLI with OAuth flow
   gh auth login
   
   # Select:
   # - GitHub.com
   # - HTTPS
   # - Login with a web browser
   # - Complete OAuth flow in browser
   
   # During OAuth flow, GitHub will request these scopes:
   # ✅ repo (Full control of private repositories)
   # ✅ read:org (Read org and team membership)
   # ✅ workflow (Update GitHub Action workflows)
   # ✅ read:user (Read user profile data)
   # ✅ user:email (Access user email addresses)
   
   # View your OAuth token
   gh auth token
   ```

2. **Copy the OAuth token** (starts with `gho_`)
   - This token has all necessary scopes from OAuth flow
   - Automatically includes `repo`, `read:org`, `workflow` and other required permissions
   - These scopes are granted during the browser OAuth authorization

3. **Add the token to repository secrets** as `COPILOT_OAUTH_TOKEN`:
   ```
   Settings → Secrets and variables → Actions → New repository secret
   Name: COPILOT_OAUTH_TOKEN
   Value: <your-oauth-token-from-gh-auth-token>
   ```

**⚠️ Why Personal Access Tokens (PAT) Don't Work for Agent:**

**Personal Access Token (Classic):**
- Works for Copilot CLI Q&A workflow
- Does NOT work for `gh agent-task` command
- Missing OAuth-specific authentication mechanism
- `gh auth login --with-token` with PAT lacks full OAuth scopes

**Personal OAuth Token (from `gh auth login`):**
- Generated through official GitHub CLI OAuth flow
- Has all necessary scopes and permissions
- Works with `gh agent-task` command
- Properly authenticated for autonomous agent operations

**OAuth Applications & GitHub Apps:**
- Not designed for this use case
- Missing required authentication flows
- Cannot be used with `gh auth login`

**✅ Best Practices for OAuth Tokens:**
- Token format starts with `gho_` (OAuth token)
- Generate using `gh auth login` command
- Tokens expire based on GitHub settings (typically 90 days)
- Regularly refresh tokens using `gh auth refresh`
- Consider creating a dedicated service account
- Monitor token usage in audit logs
- Keep tokens secure - never commit to repository

> **Security Note**: Only repository owners/admins can add secrets. Contributors cannot override the configured tokens due to branch protection and secret permissions.

## 💻 Usage

### 🎯 Copilot Q&A

Ask questions and get answers saved to the `copilot-responses` branch:

```bash
gh workflow run copilot-qa.yml \
  -f question="How do I implement OAuth 2.0 authentication in Python?"
```

**What it does:**
1. Sends your question to GitHub Copilot CLI
2. Saves the response to `response.md` 
3. Archives a timestamped copy in `responses/` directory
4. Commits both files to the `copilot-responses` branch (not main)
5. Makes response available as downloadable artifact

**Response saved to `copilot-responses` branch:**
- `response.md` - Latest response (overwritten each time)
- `responses/response_YYYYMMDD_HHMMSS.md` - Archived copy with timestamp

**Example questions:**
```bash
# Ask about implementation
gh workflow run copilot-qa.yml \
  -f question="How do I implement rate limiting in Python using decorators?"

# Ask about best practices
gh workflow run copilot-qa.yml \
  -f question="What are the best practices for error handling in REST APIs?"

# Ask for code examples
gh workflow run copilot-qa.yml \
  -f question="Show me how to implement a simple caching system in Python"
```

### 🤖 Copilot Coding Agent

Let GitHub Copilot Agent autonomously create code and pull requests:

```bash
gh workflow run copilot-agent-task.yml \
  -f task_description="Create a function to sort arrays" \
  -f base_branch="main"
```

**What it does:**
1. Runs GitHub Copilot Coding Agent with your task description
2. Agent autonomously analyzes the task and creates appropriate code
3. Agent creates a new branch and commits the code changes
4. Agent opens a pull request with the implementation
5. You receive notifications when the PR is ready for review
6. Agent can continue working on the task based on feedback

**Example tasks:**
```bash
# Create utility functions
gh workflow run copilot-agent-task.yml \
  -f task_description="Create a utility function for data validation with email and phone number checking"

# Implement features
gh workflow run copilot-agent-task.yml \
  -f task_description="Implement a REST API endpoint for user authentication with JWT tokens"

# Add tests
gh workflow run copilot-agent-task.yml \
  -f task_description="Add comprehensive unit tests for the existing calculator functions"

# Fix bugs
gh workflow run copilot-agent-task.yml \
  -f task_description="Fix the memory leak in the image processing module"
```

**Agent Workflow:**
1. 🔍 **Analysis**: Agent analyzes your task and repository structure
2. 🏗️ **Planning**: Creates a plan for implementing the requested changes
3. 💻 **Coding**: Writes code following best practices and repository patterns
4. 🧪 **Testing**: May add tests if appropriate for the task
5. 📝 **Documentation**: Updates documentation as needed
6. 🔄 **Review**: Opens PR for human review and feedback
7. 🔁 **Iteration**: Can continue working based on review feedback

## 📁 Project Structure

```
.
├── .github/
│   ├── workflows/
│   │   ├── copilot-qa.yml                      # Q&A workflow (active)
│   │   ├── copilot-agent-task.yml              # Coding Agent workflow (active)
│   │   ├── copilot-feature-dev.yml.disabled    # Code generation (disabled)
│   │   └── codeql.yml                          # Security scanning (disabled - no Python code)
│   ├── dependabot.yml                          # Dependency updates configuration
│   └── CODEOWNERS                              # Code review assignments
├── responses/                                   # Copilot Q&A responses (in copilot-responses branch)
│   └── response_YYYYMMDD_HHMMSS.md
├── response.md                                  # Latest Q&A response (in copilot-responses branch)
├── SECURITY.md                                  # Security policy and vulnerability reporting
├── .gitignore                                   # Includes protection against secrets leakage
├── LICENSE                                      # MIT License
└── README.md                                    # This file
```

## 📊 Example Output

### Q&A Response Format

Responses are saved in markdown format in the `copilot-responses` branch:

```markdown
# Copilot Response

**Question:** How do I implement rate limiting in Python?

**Asked:** 2025-10-17 10:30:45 UTC

---

[Copilot's detailed answer with code examples...]
```

### Coding Agent Output

The Coding Agent creates pull requests with detailed descriptions:

```markdown
## 🤖 AI-Generated Feature

**Task:** Create a function to sort arrays
**Agent:** GitHub Copilot Coding Agent  
**Branch:** copilot-agent/sort-arrays-1729234567

### Changes Made
- Added `utils/sorting.py` with multiple sorting algorithms
- Implemented quicksort, mergesort, and heapsort functions
- Added comprehensive error handling and input validation
- Included docstrings and type hints
- Added unit tests in `tests/test_sorting.py`

### Testing
✅ All tests pass  
✅ Code follows project style guidelines  
✅ Documentation updated

**Ready for review!**
```

## 🎯 Use Cases

### Q&A Workflow
1. **Knowledge Base**: Build a repository of Q&A responses in a dedicated branch
2. **Documentation Assistant**: Query technical documentation on-demand  
3. **Learning Tool**: See how Copilot explains common patterns and best practices
4. **Team Resource**: Share Copilot insights with team members through organized responses

### Coding Agent Workflow  
1. **Feature Development**: Let the agent implement new features autonomously
2. **Bug Fixes**: Describe bugs and let the agent research and fix them
3. **Code Refactoring**: Ask the agent to improve existing code quality
4. **Test Creation**: Generate comprehensive test suites for existing code
5. **Documentation**: Auto-generate documentation and examples
6. **Prototype Development**: Quickly prototype new ideas and concepts

### Combined Workflow
1. **Research Phase**: Use Q&A to understand requirements and best practices
2. **Implementation Phase**: Use Coding Agent to implement the actual solution
3. **Review Phase**: Maintain clean main branch with branch protection and code review

## 🔍 Validation

Install the YAML validator for workflow syntax checking:

```bash
npm install -g @action-validator/cli
action-validator .github/workflows/copilot-qa.yml
```

## 🔒 Security Features

This repository includes comprehensive security configuration:

- **SECURITY.md**: Vulnerability disclosure policy and reporting instructions
- **Dependabot**: Automated dependency updates for Python and GitHub Actions
- **CODEOWNERS**: Automatic code review assignment
- **Branch Protection**: Main branch requires pull requests with reviews
- **Secret Scanning**: Prevents accidental commit of credentials and tokens
- **.gitignore**: Extended rules to prevent secrets leakage

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [GitHub Copilot](https://github.com/features/copilot) - AI pair programmer
- [GitHub Actions](https://github.com/features/actions) - CI/CD platform
- [@github/copilot](https://www.npmjs.com/package/@github/copilot) - Copilot CLI

## 📚 Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub CLI Documentation](https://cli.github.com/manual/)

## 🐛 Troubleshooting

### Q&A Workflow Issues

#### Workflow fails with "COPILOT_TOKEN not found"
- Ensure you've created a PAT with Copilot scope
- Add it as a secret named `COPILOT_TOKEN` in repository settings

#### Can't push to main branch
- This is expected - main branch is protected
- Responses are saved to `copilot-responses` branch automatically
- For other changes, create a feature branch and open a PR

#### Where are my Q&A responses?
- Check the `copilot-responses` branch
- Responses are not committed to `main` due to branch protection

### Coding Agent Issues

#### Workflow fails with "COPILOT_OAUTH_TOKEN not found"
- Ensure you've created a Personal OAuth Token using `gh auth login`
- Add it as a secret named `COPILOT_OAUTH_TOKEN` in repository settings
- OAuth token must start with `gho_` prefix

#### "gh agent-task command not available"
- GitHub CLI version must be 2.80.0 or later
- Update GitHub CLI: `gh extension upgrade cli` or reinstall

#### Agent doesn't create a PR
- Check if task description is specific enough
- Verify the base branch exists
- Check agent logs artifact for error details
- Some tasks may not require code changes

#### Token authentication fails - "Not a valid OAuth token"
- **Most common issue**: Using Personal Access Token (PAT) instead of Personal OAuth Token
- **Solution**: Generate OAuth token using `gh auth login` command, then get token with `gh auth token`
- ❌ PAT (starts with `ghp_` or `github_pat_`) - **doesn't work for Agent**
- ✅ OAuth token (starts with `gho_`) - **required for Agent**
- Personal Access Tokens work for Copilot CLI Q&A, but NOT for Copilot Agent

#### "gh auth login --with-token" fails
- Cannot use `gh auth login --with-token` with Personal Access Token
- PAT lacks full OAuth authentication mechanism required by `gh agent-task`
- **Solution**: Use interactive `gh auth login` with browser OAuth flow:
  ```bash
  gh auth login  # Select GitHub.com, HTTPS, login with browser
  gh auth token  # Copy this token for COPILOT_OAUTH_TOKEN secret
  ```

#### Why doesn't my PAT work for the Agent?
- Copilot CLI (Q&A) uses PAT with `copilot` scope ✅
- Copilot Agent uses OAuth token from `gh auth login` flow ✅
- These are **different authentication mechanisms**
- PAT = Personal Access Token (created manually on github.com)
- OAuth Token = Generated through GitHub CLI OAuth flow (via `gh auth login`)

### General Issues

#### GitHub CLI authentication problems
- Run `gh auth status` to check authentication
- Re-authenticate with `gh auth login`
- Verify token permissions in GitHub settings

---

Made with ❤️ using GitHub Copilot CLI
