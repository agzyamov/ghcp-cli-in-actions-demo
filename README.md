# GitHub Copilot CLI in Actions Demo

> Automate your software development lifecycle with GitHub Copilot CLI in GitHub Actions

[![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-blue?logo=github-actions)](https://github.com/features/actions)
[![Copilot](https://img.shields.io/badge/GitHub-Copilot-purple?logo=github)](https://github.com/features/copilot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Overview

This repository demonstrates how to integrate GitHub Copilot CLI into GitHub Actions workflows. Ask technical questions and get AI-powered answers automatically saved to a dedicated branch, with comprehensive security features to protect your repository.

## ✨ Features

- 📝 **Interactive Q&A**: Ask questions and get answers saved to a dedicated branch
- � **Security First**: Comprehensive security configuration with Dependabot, CODEOWNERS, and secret scanning
- 🎯 **Zero Configuration**: Works out of the box with GitHub Actions
- 🛡️ **Protected Main Branch**: Branch protection rules enforce code review workflow

## 📋 Prerequisites

- GitHub repository with Actions enabled
- GitHub Copilot subscription
- Personal Access Token (PAT) with Copilot scope

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

The repository owner needs to create a Personal Access Token with Copilot access:

1. Create a [Personal Access Token](https://github.com/settings/tokens/new) with these scopes:
   - `repo` (Full control of private repositories)
   - `copilot` (Access to Copilot features)

2. Add to repository secrets as `COPILOT_TOKEN`:
   ```
   Settings → Secrets and variables → Actions → New repository secret
   Name: COPILOT_TOKEN
   Value: <your-token>
   ```

> **Security Note**: Only repository owners/admins can add secrets. Contributors cannot override the configured token due to branch protection and secret permissions.

## 💻 Usage

### � Copilot Q&A

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

## 📁 Project Structure

```
.
├── .github/
│   ├── workflows/
│   │   ├── copilot-qa.yml                      # Q&A workflow (active)
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

## 🎯 Use Cases

1. **Knowledge Base**: Build a repository of Q&A responses in a dedicated branch
2. **Documentation Assistant**: Query technical documentation on-demand
3. **Learning Tool**: See how Copilot explains common patterns and best practices
4. **Team Resource**: Share Copilot insights with team members through organized responses
5. **Protected Workflow**: Maintain clean main branch with branch protection and code review

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

### Workflow fails with "COPILOT_TOKEN not found"
- Ensure you've created a PAT with Copilot scope
- Add it as a secret named `COPILOT_TOKEN` in repository settings

### Can't push to main branch
- This is expected - main branch is protected
- Responses are saved to `copilot-responses` branch automatically
- For other changes, create a feature branch and open a PR

### Where are my Q&A responses?
- Check the `copilot-responses` branch
- Responses are not committed to `main` due to branch protection

---

Made with ❤️ using GitHub Copilot CLI
